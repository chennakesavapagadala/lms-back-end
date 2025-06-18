from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Assignment, Submission  # Import your Course model

admin.site.register(Assignment)
admin.site.register(Submission)  # Register your model to be available in the admin panel
