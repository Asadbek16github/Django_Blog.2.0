from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CostomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class Signup_View(CreateView):
    form_class = CostomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')