
from django.urls import path

from . import views 

urlpatterns = [
  path('dashboard/',views.dashboard,name='dashboard'),
  path('create-profile/',views.create_profile ,name='create_profile'),
  path('register/',views.register,name="register"),
  path('login/',views.login_page ,name='login'),
  path('logout/',views.logout_page ,name='logout'),
  path('profiles/',views.profiles ,name='profiles'),
  path('profile/<str:username>/',views.profile ,name='profile'),

  path('experience/add',views.add_experience ,name='addexperience'),
  path('experience/detail/<int:id>',views.detail_experience ,name='detailexperience'),
  path('experience/delete/<int:id>',views.delete_experience ,name='deleteexperience'),
  path('experience/update/<int:id>',views.update_experience ,name='updateexperience'),

  path('education/add',views.add_education ,name='addeducation'),
  path('education/delete/<int:id>',views.delete_education ,name='deleteeducation'),
  path('education/update/<int:id>',views.update_education ,name='updateeducation'),

  path('message',views.message ,name='message'),

]