from cProfile import label
import email
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'name': 'Your Name',
            'email':'Your Email',
            'comment':'Your Comment'
        }