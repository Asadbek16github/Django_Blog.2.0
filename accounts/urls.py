from django.urls import path
from .views import Signup_View

urlpatterns = [
    path('signup/', Signup_View.as_view(), name='signup')
]