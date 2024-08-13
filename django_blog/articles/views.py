from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from .models import Article
from django.http import Http404


class ArticlesListView(TemplateView):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = [
            {'id': 1, 'title': 'Templates', 'content': 'Something about templates'},
            {'id': 2, 'title': 'Views', 'content': 'Something about views'},
            {'id': 3, 'title': 'Other', 'content': 'Something about anything'},
        ]
        return context


class ArticleDetailView(TemplateView):
    template_name = 'articles/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = 'python'
        context['article_id'] = '42'
        return context
