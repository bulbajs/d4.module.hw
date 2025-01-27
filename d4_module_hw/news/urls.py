from django.urls import path
from .views import PostList, PostDetail, NewsCreateView, ArticleCreateView,UpdateNews, UpdateArticle, DeleteNews, DeleteArticle


urlpatterns = [
    path('', PostList.as_view(), name='news_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', UpdateNews.as_view(), name='news_edit'),
    path('article/<int:pk>/edit/', UpdateArticle.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', DeleteNews.as_view(), name='news_delete'),
    path('article/<int:pk>/delete/', DeleteArticle.as_view(), name='article_delete'),
]

