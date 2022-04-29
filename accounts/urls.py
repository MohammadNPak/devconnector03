from sqlite3 import register_adapter
from django.urls import path

from .views import create_profile,dashboard,register



urlpatterns = [
  path('dashboard',dashboard,name='dashboard'),
  path('create-profile',create_profile ,name='create_profile'),
  path('register',register,name="register")
]