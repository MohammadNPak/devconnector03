
from django.urls import path

from .views import (login_page, profiles ,
             profile,create_profile,dashboard,register)

urlpatterns = [
  path('dashboard',dashboard,name='dashboard'),
  path('create-profile',create_profile ,name='create_profile'),
  path('register',register,name="register"),
  path('login',login_page ,name='login'),
  path('profiles',profiles ,name='profiles'),
  path('profile',profile ,name='profile'),

]