from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('customers/',views.customers, name="customers")
]
