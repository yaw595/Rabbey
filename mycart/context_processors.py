from .mycart import Cart


def mycart(request):
    return {'mycart': Cart(request)}
