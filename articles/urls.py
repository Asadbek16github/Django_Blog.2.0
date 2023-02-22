from django.urls import path
from .views import ArticlesView, ArticleDetailView

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='articleDetail'),
    path('', ArticlesView.as_view(), name='articlesPage'),
]