from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from django.contrib import messages
from .forms import ArticleForm
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


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'articles/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article has been created!')
            return redirect(reverse('articles'))
        messages.error(request, form.errors)
        return render(
            request,
            'articles/create.html',
            {'form': form}
        )
