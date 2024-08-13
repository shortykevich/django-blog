from django.urls import path
from django_blog.articles import views


app_name = 'articles'


urlpatterns = [
    path('', views.ArticlesIndexView.as_view(), name='list'),
    path('<str:tag>/<int:article_id>/', views.ArticleDetailView.as_view(), name='article'),
]
