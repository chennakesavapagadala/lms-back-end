# assignments/urls.py

from django.urls import path
from .views import AssignmentListCreateAPIView, SubmissionListCreateAPIView

urlpatterns = [
    path('', AssignmentListCreateAPIView.as_view(), name='assignment'),
    path('submissions/', SubmissionListCreateAPIView.as_view(), name='submission'),
]
