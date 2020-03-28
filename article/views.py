from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'detail_page'


def edit_page(request):
    template = 'edit_page.html'
    context = {
        'list_articles': Article.objects.all().order_by('-id')
    }
    return render(request, template, context)