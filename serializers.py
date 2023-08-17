from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


from lessons.models import Course, Lesson
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    number_of_lessons = SerializerMethodField()
    def get_number_of_lessons(self, course):
        return Course.objects.filter(lesson=course.lesson).count()


    class Meta:
        model = Course
        fields = '__all__'
