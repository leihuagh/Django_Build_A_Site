from django.shortcuts import render
from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, "auth/login.html", context)


def logout_view(request):
    return render(request, "auth/logout.html", {})
