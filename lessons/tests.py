
from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase

from lessons.models import Lesson, Course


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
            'lesson/create/',
            data = data
        )
        print(response)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)