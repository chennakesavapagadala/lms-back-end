# enrollments/views.py

from rest_framework import generics, permissions
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
from django.shortcuts import render

# Create your views here.
