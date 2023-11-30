from django.shortcuts import render, get_object_or_404
from cart.models import Cart, CartItem, Order
from products.models import Product


def show_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)
    context = {"carrito": cart, "items": items}
    return render(request, "cart/show_cart.html", context)
