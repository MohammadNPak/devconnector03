from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    bio = models.TextField()
    github_username = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    

class SocialMedia(models.Model):
    TYPES = (
        ('w', 'web'),
        ('f', 'facebook'),
        ('t', 'twitter'),
        ('l', 'linked in'),
        ('i', 'instagram'),
    )
    url = models.URLField()
    type = models.CharField(max_length=1,choices=TYPES)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    user=models.ManyToManyField(User)


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    from_date = models.DateField()
    to_date=models.DateField()
    current_job = models.BooleanField()
    decription = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date=models.DateField()
    current_school = models.BooleanField()
    decription = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

class Github(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    star = models.PositiveIntegerField()
    watcher = models.PositiveIntegerField()
    fork = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    