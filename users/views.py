# users/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny  # <- use auth now
from .models import CustomUser
from .serializers import UserSerializer
from .tasks import send_welcome_email

from django.shortcuts import render, redirect

def homeView(request):

    return render(request, 'rest_framework/home.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View



