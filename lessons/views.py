from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from lessons.models import Course, Lesson
from lessons.paginators import LessonPaginator
from lessons.permissions.permissions import IsOwner, IsModerator
from serializers import CourseSerializer, LessonSerializer, MyTokenObtainPairSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

@login_required(login_url='/users/login')
def secure(request):
    user = request.user
    return render(request, 'secure.html', {'email': user.email})


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    #permission_classes = (IsAuthenticated)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    #permission_classes = [AllowAny]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson_name', 'way_of_payment')
    ordering_fields = ('date_of_payment')
    #permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner | IsModerator]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    #permission_classes = (IsAuthenticated)