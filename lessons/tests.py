from unittest import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase

from lessons.models import Lesson, Course
from users.models import User

class LessonTest(APITestCase):

    def create_member(self):
        """Creates a new MEMBER user"""
        # Create test user with MEMBER role
        self.user_member = User.objects.create(
            email='test@gmail.com',
            is_active=True,
        )
        self.user_member.set_password('test')
        self.user_member.save()

    def create_moderator(self):
        """Creates a new MODERATOR user"""
        # Create test user with MEMBER role
        self.user_moderator = User.objects.create(
            email='test2@gmail.com',
            is_active=True,
            role='moderator'
        )
        self.user_moderator.set_password('test')
        self.user_moderator.save()

    def setUp(self) -> None:
        """Set up initial objects for each test"""
        # Create MEMBER user
        self.create_member()
        # Create MODERATOR user
        self.create_moderator()

        # Create Course object
        self.course = Course.objects.create(
            course_name='2',
            description='course description'
        )
        # Create Lesson object
        self.lesson = Lesson.objects.create(
            lesson_name='test lesson',
            description='lesson description',
            course=self.course,
            owner=self.user_member
        )

    def test_create_lesson(self):
        """Testing lesson creation"""
        # Authenticate user without token
        self.client.force_authenticate(self.user_member)

        data = {
            'lesson_name': 'test lesson2',
            'description': 'lesson2 description',
            'course': self.course.id,
        }
        # Create second lesson
        response = self.client.post(
            reverse("courses:lesson-create"),
        )