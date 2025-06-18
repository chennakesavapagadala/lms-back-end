# courses/urls.py

from rest_framework.routers import DefaultRouter
from .views import CourseViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]
