import django_filters
from django_filters import FilterSet, DateTimeFilter, CharFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    time_in_Post = DateTimeFilter(field_name='time_in_Post', lookup_expr='gte', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Post
        fields = ['title', 'categoryType', 'time_in_Post']
