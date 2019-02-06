from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from core.utils import check_authentication
from django.views.generic import ListView
from products.models import Product


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
    context = check_authentication(request, context)
    return render(request, 'list.html', context)