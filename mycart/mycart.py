from decimal import Decimal
from django.conf import settings
from cart.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        mycart = self.session.get(settings.CART_SESSION_ID)
        if not mycart:
            mycart = self.session[settings.CART_SESSION_ID] = {}
        self.mycart = mycart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.mycart:
            self.mycart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.mycart[product_id]['quantity'] = quantity
        else:
            self.mycart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.mycart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.mycart:
            del self.mycart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.mycart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.mycart[str(product.id)]['product'] = product

        for item in self.mycart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.mycart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.mycart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
