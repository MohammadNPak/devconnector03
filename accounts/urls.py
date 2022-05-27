
from django.urls import path

from . import views 

urlpatterns = [
  path('dashboard',views.dashboard,name='dashboard'),
  path('create-profile',views.create_profile ,name='create_profile'),
  path('register',views.register,name="register"),
  path('login',views.login_page ,name='login'),
  path('profiles',views.profiles ,name='profiles'),
  path('profile',views.profile ,name='profile'),
  path('addeducation',views.add_education ,name='education'),
  path('addexperience',views.add_experience ,name='experience'),

]