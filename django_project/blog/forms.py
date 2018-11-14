from .models import Question,  Answer
from django.forms import ModelForm


class PostForm(ModelForm):
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


