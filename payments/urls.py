# payments/urls.py

from django.urls import path
from .views import PaymentListCreateAPIView, StripeCheckoutSessionAPIView

urlpatterns = [
    path('', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('create-checkout-session/', StripeCheckoutSessionAPIView.as_view(), name='stripe-checkout'),
]
