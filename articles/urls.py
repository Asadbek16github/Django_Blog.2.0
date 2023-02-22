from django.urls import path
from .views import ( 
                        ArticlesView, 
                        ArticleDetailView, 
                        ArticleDeleteView, 
                        ArticleUpdateView,
                        ArticleCreateView
                    )

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='articleDetail'),
    path('', ArticlesView.as_view(), name='articlesPage'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='deleteObject'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='updateObject'),
    path('create/', ArticleCreateView.as_view(), name='createObject'), 
]