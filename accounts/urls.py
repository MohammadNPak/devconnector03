from django.urls import path
from .views import login_page, profiles , profile

urlpatterns = [
    path('login',login_page ,name='login url'),
    path('profiles',profiles ,name='profiles'),
    path('profile',profile ,name='profile'),
]