# users/urls.py

from django.urls import path
from .views import RegisterView, LoginView, getUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/', getUserView.as_view(), name='user')
]
