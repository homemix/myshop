from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    pass
