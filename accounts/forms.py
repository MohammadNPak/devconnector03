import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserForm(UserCreationForm):
    class Meta:
        model=models.User
        fields=['username','email']

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model=models.SocialMedia
        # fields=['']
        exclude = ('user',)
        
class SkillForm(forms.ModelForm):
    class Meta:
        model=models.Skill
        fields=['name']
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model=models.Experience
        # fields=[]
        exclude = ('user',)
        
class EducationForm(forms.ModelForm):
    class Meta:
        model=models.Education
        # fields=[]
        exclude = ('user',)
        
# class GithubForm(forms.ModelForm):
#     class Meta:
#         model=models.Github
#         fields=[]

    

