from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Home_page_View(TemplateView):
    template_name="index.html"
