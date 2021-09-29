from django import forms
from django.db import models
from django.forms import fields
from.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content', )