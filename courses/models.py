from django.db import models

# Create your models here.
# courses/models.py

from django.db import models
from users.models import CustomUser

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
