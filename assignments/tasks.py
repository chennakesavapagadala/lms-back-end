# assignments/tasks.py

from celery import shared_task

@shared_task
def auto_grade_assignment(assignment_id):
    # Your grading logic
    pass


# assignments/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from .models import Assignment
from datetime import date, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_assignment_reminders():
    tomorrow = date.today() + timedelta(days=1)
    assignments_due = Assignment.objects.filter(due_date=tomorrow)

    for assignment in assignments_due:
        enrolled_users = assignment.course.enrollments.all().values_list('user__email', flat=True)
        for email in enrolled_users:
            send_mail(
                subject='Assignment Due Reminder',
                message=f"The assignment '{assignment.title}' is due tomorrow!",
                from_email='admin@lms.com',
                recipient_list=[email],
                fail_silently=False,
            )
