from django.urls import path
from .views import Home_page_View

urlpatterns = [
    path('', Home_page_View.as_view(), name='home')
]