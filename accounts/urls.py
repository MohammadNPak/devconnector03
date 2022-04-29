from django.urls import path
from .views import create_profile,dashboard



urlpatterns = [
  path('dashboard',dashboard,name='dashboard'),
  path('create-profile',create_profile ,name='create_profile'),

]