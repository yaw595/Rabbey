from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.models import Product
from .mycart import Cart
from .forms import CartAddProductForm


@require_POST
def mycart_add(request, product_id):
    mycart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        mycart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('mycart:mycart_detail')


def mycart_remove(request, product_id):
    mycart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    mycart.remove(product)
    return redirect('mycart:mycart_detail')


def mycart_detail(request):
    mycart = Cart(request)
    for item in mycart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'mycart/detail.html', {'mycart': mycart})
