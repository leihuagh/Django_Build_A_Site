from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')

    return render(request, "auth/login.html", context)


def logout_view(request):
    return render(request, "auth/logout.html", {})
