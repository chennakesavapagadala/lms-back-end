from django.db import models

# Create your models here.
# payments/models.py

from django.db import models
from django.conf import settings
from courses.models import Course

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100)  # Stripe payment ID or similar
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} paid {self.amount} for {self.course}'
