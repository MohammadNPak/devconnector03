from django.urls import path



from .views import post,posts,sample_post
urlpatterns = [
  path('post/<int:id>',post ,name='post'),
  path('posts',posts ,name='posts'),
  path('sample_post',sample_post ,name='sample_post'),

]