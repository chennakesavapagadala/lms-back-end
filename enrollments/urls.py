# enrollments/urls.py

from django.urls import path
from .views import EnrollmentListCreateAPIView

urlpatterns = [
    path('', EnrollmentListCreateAPIView.as_view(), name='enrollment-list'),
]
