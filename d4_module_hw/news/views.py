from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator


class PostList(ListView):
    model = Post
    ordering = 'time_in_Post'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
