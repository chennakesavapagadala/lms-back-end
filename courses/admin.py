from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course  # Import your Course model

admin.site.register(Course)  # Register your model to be available in the admin panel
