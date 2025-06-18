# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from enrollments.models import Enrollment
# from users.models import CustomUser
# from courses.models import Course

# class EnrollmentModelTest(TestCase):
#     def test_create_enrollment(self):
#         user = CustomUser.objects.create_user(username='john', password='pass1234', role='student')
#         course = Course.objects.create(name='Django Basics', description='Intro to Django')
#         enrollment = Enrollment.objects.create(user=user, course=course)

#         # Assertions
#         self.assertEqual(enrollment.user, user)
#         self.assertEqual(enrollment.course, course)

# from django.test import TestCase
# from enrollments.models import Enrollment
# from enrollments.serializers import EnrollmentSerializer
# from users.models import CustomUser
# from courses.models import Course

# class EnrollmentSerializerTest(TestCase):
#     def test_enrollment_serializer(self):
#         user = CustomUser.objects.create_user(username='john', password='pass1234', role='student')
#         course = Course.objects.create(name='Django Basics', description='Intro to Django')
#         enrollment = Enrollment.objects.create(user=user, course=course)

#         # Serialize the enrollment
#         serializer = EnrollmentSerializer(enrollment)

#         # Assertions
#         self.assertEqual(serializer.data['user'], user.id)
#         self.assertEqual(serializer.data['course'], course.id)

# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from users.models import CustomUser
# from courses.models import Course

# class EnrollmentViewSetTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = CustomUser.objects.create_user(username='john', password='pass1234', role='student')
#         self.course = Course.objects.create(name='Django Basics', description='Intro to Django')
#         self.enrollment_data = {'user': self.user.id, 'course': self.course.id}

#     def test_create_enrollment(self):
#         # Post request to create an enrollment
#         response = self.client.post(reverse('enrollment-list'), self.enrollment_data, format='json')

#         # Assertions
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['user'], self.user.id)
#         self.assertEqual(response.data['course'], self.course.id)
