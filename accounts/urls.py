from sqlite3 import register_adapter
from django.urls import path
from .views import register
urlpatterns = [
    path('register',register)
]