from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView


# Create your views here.
class ProductList(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 5
    template_name = 'products/list.html'


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})


def product_detail(request, category, owner, slug):
    product = get_object_or_404(Product, category=category, owner=owner, slug=slug)
    return render(request, 'products/detail.html', {'product': product})
