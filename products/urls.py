from django.urls import path
from .views import list_view

app_new = 'products'
urlpatterns = [
    path('', list_view, name='product_list'),
]
