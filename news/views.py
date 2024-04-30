from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'news/index.html', {'latest_articles': latest_articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/detail.html', {'article': article})
