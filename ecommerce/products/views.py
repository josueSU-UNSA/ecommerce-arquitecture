from django.shortcuts import render
from products.models import Product, Category


def list_products(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "products/list_products.html", context)
