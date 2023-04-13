from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('shipping_returns/', views.shipping_returns, name='shipping_returns'),
    path('privacy/', views.privacy, name='privacy'),
]
