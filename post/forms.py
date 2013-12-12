from .models import Article,Comment
from django import forms


class ArticleAddForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

