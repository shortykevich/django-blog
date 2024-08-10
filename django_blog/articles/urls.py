from django.urls import path

from django_blog.articles import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='articles'),
]
