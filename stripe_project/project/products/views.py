from typing import Any

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'products/success.html'


class CancelView(TemplateView):
    template_name = 'products/cancel.html'


class GetCheckoutSessionView(View):
    def get(self, request, item_id):
        item = Item.objects.get(pk=item_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,  # Convert to cents
                        'product_data': {
                            'name': item.name
                        }
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return JsonResponse({
            'id': session.id
        })


class ItemDetailView(View):
    template_name = 'products/item_detail.html'

    def get(self, request, item_id):
        item = Item.objects.get(pk=item_id)
        print(settings.STRIPE_PUBLIC_KEY)
        context = {
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        }
        return render(request, self.template_name, context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')