# users/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer



class CustomUserModelTest(TestCase):
    def test_create_user_with_role(self):
        user = CustomUser.objects.create_user(
            username='john', password='pass1234', role='student'
        )
        self.assertEqual(user.role, 'student')
        self.assertTrue(user.check_password('pass1234'))
        self.assertEqual(str(user), 'john')

class CustomUserSerializerTest(TestCase):
    def test_user_serializer(self):
        user = CustomUser.objects.create_user(username='john', password='pass1234', role='student')
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data['username'], 'john')
        self.assertEqual(serializer.data['role'], 'student')

class UserViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = CustomUser.objects.create_user(
            username='adminuser', password='adminpass', role='admin', is_staff=True
        )
        refresh = RefreshToken.for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

        self.user_data = {
            'username': 'john',
            'password': 'pass1234',
            'role': 'student'
        }

    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'john')
        self.assertEqual(response.data['role'], 'student')
