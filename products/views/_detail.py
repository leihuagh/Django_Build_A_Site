from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from core.utils import check_authentication
from django.views.generic import ListView
from products.models import Product


def detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product
    }
    context = check_authentication(request, context)
    return render(request, 'detail.html', context)
