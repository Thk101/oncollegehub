from .models import Question, Answer
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):
    title = forms.CharField(max_length=40, min_length=12)

    class Meta:
        model = Question
        exclude = ('author',)
        fields = ['title', 'content']
        labels = {
            "title": "Title",
            "content": "Body",
        }


class CommentForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('author', 'post')
        fields = ['content']
