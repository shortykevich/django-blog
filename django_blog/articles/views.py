from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(
        request,
        'articles/index.html',
        context={
            'articles': [
                {'title': 'Templates', 'content': 'Something about templates'},
                {'title': 'Views', 'content': 'Something about views'},
                {'title': 'Other', 'content': 'Something about anything'},
            ]}
    )
