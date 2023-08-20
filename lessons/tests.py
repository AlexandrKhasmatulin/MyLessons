from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from lessons.models import Lesson, Course


# Create your tests here.
class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.description = Lesson.objects.create(
            description = 'Lesson about Pagination'
        )
        self.lesson = Lesson.objects.create(
            name='Pagination',
            description = self.description

        )
    def test_LessonListAPIView(self):
        response = self.client.get(
            reverse('lessons:lesson-list')
        )
        self.assertEqual(
            response.status_code,
            status = HTTP_200_OK
        )