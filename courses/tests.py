from django.test import TestCase

# Create your tests here.
from django.test import TestCase #common for models,serializers, views
from courses.models import Course #common for models,serializers, views
from .models import CustomUser
class CourseModelTest(TestCase):
    def test_create_course(self):
        # create instructor
        instructor = CustomUser.objects.create_user(
            username='kesava',
            password='testpass123',
            role='instructor'
        )
        # Create a course
        course = Course.objects.create(title='Django Basics', description='Intro to Django', instructor=instructor)

        # Assertions
        self.assertEqual(course.title, 'Django Basics')
        self.assertEqual(course.description, 'Intro to Django')
        self.assertEqual(course.instructor,instructor)


from courses.serializers import CourseSerializer

class CourseSerializerTest(TestCase):
    def test_course_serializer(self):
        # create instructor
        instructor = CustomUser.objects.create_user(
            username='kesava',
            password='testpass123',
            role='instructor'
        )
        # Create a course
        course = Course.objects.create(title='Django Basics', description='Intro to Django',instructor=instructor)

        # Serialize the course
        serializer = CourseSerializer(course)

        # Assertions
        self.assertEqual(serializer.data['title'], 'Django Basics')
        self.assertEqual(serializer.data['description'], 'Intro to Django')
        self.assertEqual(serializer.data['instructor'], instructor.id)


from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from users.models import CustomUser
from courses.models import Course
from rest_framework_simplejwt.tokens import RefreshToken

class CourseViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create instructor user
        self.instructor = CustomUser.objects.create_user(
            username='instructor1',
            password='testpass123',
            role='instructor'
        )

        # Generate JWT token
        refresh = RefreshToken.for_user(self.instructor)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        # Valid course data
        self.course_data = {
            'title': 'Django Basics',
            'description': 'Intro to Django',
            'instructor': self.instructor.id
        }

    def test_create_course(self):
        url = reverse('course-list')  # DRF router path
        response = self.client.post(url, self.course_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Django Basics')
        self.assertEqual(response.data['description'], 'Intro to Django')
        self.assertEqual(response.data['instructor'], self.instructor.id)
