from django.shortcuts import render
from core.utils import check_authentication
from .forms import ContactForm


def index(request):
    context = {}
    context = check_authentication(request, context)
    return render(request, 'index.html', context)


def about(request):
    context = {}
    context = check_authentication(request, context)
    return render(request, 'about.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }
    context = check_authentication(request, context)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, 'contact.html', context)
