from django.urls import path
from rest_framework.routers import DefaultRouter
from shipments_app import views

router = DefaultRouter()

urlpatterns = [
    path('shipping_methods', views.shipping_method_api),
    path('shipping_method/<int:id>', views.shipping_method_api),

    path('customers', views.customer_api),
    path('customer/<int:id>', views.customer_api),

    path('orders', views.order_api),
    path('order/<int:id>', views.order_api)
]
