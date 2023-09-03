from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.generics import get_object_or_404

from lessons.models_lessons import Course, Lesson
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from lessons.tasks import about_subscription
from lessons.validators import validator_prohibited_link
from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token


class LessonSerializer(serializers.ModelSerializer):
    linkvideo = serializers.URLField(validators=[validator_prohibited_link], read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    lesson = LessonSerializer()
    number_of_lessons = SerializerMethodField()

    def subscription(self, validated_data, request):
        user = get_object_or_404(User, pk=request.data.get('user'))
        subscription = self.context['subscription']
        validated_data['subscription'] = subscription
        about_subscription.delay(user.username)
        return subscription

    def get_number_of_lessons(self, course):
        return Course.objects.filter(lesson=course.lesson).count()

    def payment(self, course):
        import stripe
        stripe.api_key = "sk_test_51NlIXvJ2YOyuYIQ7GNsSlk7lT6qG76Bq94vEU7pLeDUMfzM0tC5UIwZReTkWiCWlAF4gOTCjvoc0amzEis6ZerQK00zVXofPkF"
        stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 8,
                "exp_year": 2020,
                "cvc": "314",
            },
        )
        stripe.PaymentMethod.retrieve(
            "pm_1EUmzw2xToAoV8choYUtciXR",
        )

    class Meta:
        model = Course
        fields = '__all__'
