from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    bio = models.TextField()
    skill = models.ManyToManyField('Skill')
    

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


class Experience(models.Model):
    pass