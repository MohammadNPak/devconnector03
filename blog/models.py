from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

user =get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    likes = models.ManyToManyField(user, related_name="post_likes", blank=True)
    dislikes = models.ManyToManyField(user, related_name="post_dislikes", blank=True)
    
    def __str__(self) -> str:
        return f"{self.title}|{self.body[:20]}"
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.id})
    


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return f"{self.post.title}|{self.body[:40]}"


