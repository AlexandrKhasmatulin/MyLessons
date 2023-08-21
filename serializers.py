from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


from lessons.models import Course, Lesson
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from lessons.validators import validator_prohibited_link


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token

class LessonSerializer(serializers.ModelSerializer):
    linkvideo = serializers.URLField(validators=validator_prohibited_link)
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    lesson = LessonSerializer()
    number_of_lessons = SerializerMethodField()
    def subscription(self, validated_data):
        subscription = self.context['subscription']
        validated_data['subscription'] = subscription
        return subscription
    def get_number_of_lessons(self, course):
        return Course.objects.filter(lesson=course.lesson).count()


    class Meta:
        model = Course
        fields = '__all__'
