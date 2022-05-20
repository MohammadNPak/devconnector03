from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}|{self.body[:20]}"
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.id})
    


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.post.title}|{self.body[:40]}"

class SamplePost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
