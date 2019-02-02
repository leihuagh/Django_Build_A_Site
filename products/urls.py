from django.urls import path
from .views import list_view

app_name = 'products'
urlpatterns = [
    path('', list_view, name='list'),
]
