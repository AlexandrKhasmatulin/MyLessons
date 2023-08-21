from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from MyLessons import settings
from lessons.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=100, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото профиля',  **NULLABLE)
    city  = models.CharField(max_length=100, verbose_name='город',  **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class Subscription(models.Model):
    """
    Stores a single subscription to course entry, related to
    :model:`courses.Course` and to :model:`users.User` .
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name='course')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='user',
                             **NULLABLE)
