from django import forms
from .models import Post


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'time_in_Post', 'authorUser']


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'time_in_Post', 'authorUser']





