from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles
# Create your views here.

class ArticlesView(ListView):
    model = Articles
    template_name = 'article.html'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
