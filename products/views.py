from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'list.html'


def list_view(request):
    queryset = Product.objects.all().order_by('created')
    print(queryset)
    context = {
        "products": queryset,
    }
    return render(request, 'list.html', context)
