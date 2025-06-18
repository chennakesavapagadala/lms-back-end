# users/tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Welcome to LMS!',
        'Thanks for registering at our LMS platform.',
        'admin@lms.com',
        [user_email],
        fail_silently=False,
    )
