from django.urls import path
from .views import list_view

app_new = 'products'
urlpatterns = [
    path('list/', list_view, name='list_view'),
]
