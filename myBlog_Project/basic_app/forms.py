from django import forms
from basic_app.models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','slug','content','author','status')