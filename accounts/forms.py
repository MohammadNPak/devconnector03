from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields=[]

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

    

