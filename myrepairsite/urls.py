# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('sell/', views.sell, name='sell'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
]

