from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import RegisterForm


def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)

    return render(request, 'register.html', context)
