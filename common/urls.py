from django.urls import path
from .views import index, about, contact
from authentication.views import login_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
]
