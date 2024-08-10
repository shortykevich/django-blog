from django.views.generic import TemplateView


class ArticleListView(TemplateView):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = [
            {'title': 'Templates', 'content': 'Something about templates'},
            {'title': 'Views', 'content': 'Something about views'},
            {'title': 'Other', 'content': 'Something about anything'},
        ]
        return context
