from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class ArticlesView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'article.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'detail.html'


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articlesPage')

    def test_func(self):
        ob = self.get_object()
        return ob.Mualliff == self.request.user

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    template_name = 'article_update.html'
    fields = ('Sarlovha', 'Qisqacha_Matn', 'Matn', 'Rasm')
    success_url = reverse_lazy('articlesPage')

    def test_func(self):
        ob = self.get_object()
        return ob.Mualliff == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin,  CreateView):
    model = Articles
    template_name = 'article_create.html'
    fields = ('Sarlovha', 'Qisqacha_Matn', 'Matn','Rasm')
    success_url = reverse_lazy('articlesPage')

    def form_valid(self, form):
        form.instance.Mualliff = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        return self.request.user.is_superuser


