from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Article


class ArticlesIndexView(TemplateView):
    template_name = 'articles/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


class ArticleDetailView(TemplateView):
    template_name = 'articles/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = 'python'
        context['article_id'] = '42'
        return context
