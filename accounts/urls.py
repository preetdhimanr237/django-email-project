from .views import register , home
from django.urls import path

urlpatterns = [
    path('register/',register,name = 'register'),
    path('',home,name = 'home'),
]