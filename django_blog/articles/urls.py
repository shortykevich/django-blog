from django.urls import path
from django_blog.articles import views


urlpatterns = [
    path('', views.ArticlesIndexView.as_view(), name='articles'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('create/', views.ArticleFormCreateView.as_view(), name='article_create'),
]
