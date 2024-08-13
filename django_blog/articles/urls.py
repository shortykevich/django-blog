from django.urls import path
from django_blog.articles import views


app_name = 'articles'


urlpatterns = [
    path('', views.ArticlesIndexView.as_view(), name='list'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
]
