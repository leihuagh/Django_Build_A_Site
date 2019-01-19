from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, 'contact.html', {})
