from django.urls import path



from .views import post,posts
urlpatterns = [
  path('post/<int:id>',post ,name='post'),
  path('posts',posts ,name='posts'),

]