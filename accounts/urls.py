from django.urls import path
from .views import my_view,register
urlpatterns = [
    path('my_prefix',my_view ,name='my_name'),
    path('register',register,name='register')
]