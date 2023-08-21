from django.shortcuts import render
from models import Article

def articles_lists(request):
    template = 'articles/news.html'
    ordering = '-publish_date'
    articles = Article.objects.all().prefetch_related('scope').order_by(ordering)
    context = {'objects_list': articles}

    return render(request, template, context)