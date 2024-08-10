from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Кирилл'
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = ['обучение', 'программирование', 'python', 'oop']
        return context


class HomeRedirectView(RedirectView):
    url = reverse_lazy(
        'articles:article',
        kwargs={'tag': 'python', 'article_id': 42}
    )
