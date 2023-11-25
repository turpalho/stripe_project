from django.urls import path

from project.products.views import (
    SuccessView,
    CancelView,
    GetCheckoutSessionView,
    ItemDetailView
)

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('buy/<int:item_id>/', GetCheckoutSessionView.as_view(), name='get_checkout_session'),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
]
