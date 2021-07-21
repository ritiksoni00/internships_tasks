from django import forms
from django.db.models import fields
from django import forms
from .models import User, Post



class AuthForm(forms.ModelForm):
  
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'text']
