
from django import forms
from .models import Post,Comment

# class PostForm(forms.Form):
#      title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'size': '40'}))
#      body = forms.CharField(max_length=200)
#      email = forms.EmailField()
     
class PostForm(forms.ModelForm):
     class Meta:
          model=Post
          fields = ['title','body']


class CommentForm(forms.ModelForm):
     class Meta:
          model=Comment
          fields = ['body']
          widgets = {
            'body': forms.Textarea(attrs={'cols': 10, 'rows': 10,'class':"comment-body"}),
        }