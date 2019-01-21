from django.shortcuts import render


def register_view(request):
    return render(request, 'users/register.html', {})
