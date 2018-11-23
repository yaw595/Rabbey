from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from mycart.mycart import Cart


def order_create(request):
    mycart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            for item in mycart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    total=item['quantity'] * item['price']
                )
            mycart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})
