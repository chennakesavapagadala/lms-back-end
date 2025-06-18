# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from assignments.models import Assignment
# from courses.models import Course

# class AssignmentModelTest(TestCase):
#     def test_create_assignment(self):
#         course = Course.objects.create(name='Django Basics', description='Intro to Django')
#         assignment = Assignment.objects.create(course=course, title='Assignment 1', description='First assignment')

#         # Assertions
#         self.assertEqual(assignment.course, course)
#         self.assertEqual(assignment.title, 'Assignment 1')

# from django.test import TestCase
# from assignments.models import Assignment
# from assignments.serializers import AssignmentSerializer
# from courses.models import Course

# class AssignmentSerializerTest(TestCase):
#     def test_assignment_serializer(self):
#         course = Course.objects.create(name='Django Basics', description='Intro to Django')
#         assignment = Assignment.objects.create(course=course, title='Assignment 1', description='First assignment')

#         # Serialize the assignment
#         serializer = AssignmentSerializer(assignment)

#         # Assertions
#         self.assertEqual(serializer.data['course'], course.id)
#         self.assertEqual(serializer.data['title'], 'Assignment 1')
#         self.assertEqual(serializer.data['description'], 'First assignment')

        
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from courses.models import Course

# class AssignmentViewSetTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.course = Course.objects.create(name='Django Basics', description='Intro to Django')
#         self.assignment_data = {'course': self.course.id, 'title': 'Assignment 1', 'description': 'First assignment'}

#     def test_create_assignment(self):
#         # Post request to create an assignment
#         response = self.client.post(reverse('assignment'), self.assignment_data, format='json')

#         # Assertions
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['title'], 'Assignment 1')
#         self.assertEqual(response.data['description'], 'First assignment')
