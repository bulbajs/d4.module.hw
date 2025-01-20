from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = 'time_in_Post'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow()
        # context['next_sale'] = 'Убрал строку None'
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.order_by('id')

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
