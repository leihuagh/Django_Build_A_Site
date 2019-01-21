from django.urls import path, include
from .views import register_view

app_name = 'users'
urlpatterns = [
    path('register/', register_view, name='register'),
]
