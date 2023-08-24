from unittest import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase

from lessons.models import Lesson, Course
from users.models import User

class SimpleTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        User = get_user_model()
        self.client.login(email='temporary@gmail.com', password='temporary')
        response = self.client.get('/manufacturers/', follow=True)
        user = User.objects.get(email='temporary@gmail.com')
        self.assertEqual(response.context['email'], 'temporary@gmail.com')
# Create your tests here.
class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_LessonCreateAPIView(self):
        data = {
        'lesson_name':'test',
        'description':'test'
        }
        response=self.client.post(
            '/lesson/create/',
            data = data
        )
        print(response)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)
        self.assertTrue(
            Lesson.object.all().exists()
        )

    def test_LessonListAPIView(self):
        data = {
        'lesson_name':'test',
        'description':'test'
        }
        response=self.client.post(
            '/lesson/list/',
            data = data
        )
        print(response)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)