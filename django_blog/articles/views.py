from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import Article


class ArticlesIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/article.html',
            context={'article': article}
        )
