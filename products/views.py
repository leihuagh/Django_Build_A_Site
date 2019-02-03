from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'list.html'


def list_view(request):
    queryset = Product.objects.all().order_by('created')
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        "products": products,
    }
    return render(request, 'list.html', context)
