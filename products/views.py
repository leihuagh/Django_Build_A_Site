from django.shortcuts import render
from .models import Product


def list_view(request):
    queryset = Product.objects.all()
    context = {
        "objects": queryset
    }

    return render(request, 'products/list.html', context)
