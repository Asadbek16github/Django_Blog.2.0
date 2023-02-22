from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.

class ArticlesView(ListView):
    model = Articles
    template_name = 'article.html'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articlesPage')

class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'article_update.html'
    fields = ('Sarlovha', 'Qisqacha_Matn', 'Matn', 'Rasm')
    success_url = reverse_lazy('articlesPage')


class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'article_create.html'
    fields = ('Sarlovha', 'Qisqacha_Matn', 'Matn', 'Rasm', 'Mualliff')
    success_url = reverse_lazy('articlesPage')


