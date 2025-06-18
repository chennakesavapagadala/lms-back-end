from django.shortcuts import render

# Create your views here.
# courses/views.py

from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated] 
