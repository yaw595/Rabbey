from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from mycart.forms import CartAddProductForm
from .forms import ReviewForm


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'cart/products/list.html', context)


def product_detail(request, id, slug, category_slug=None):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    mycart_product_form = CartAddProductForm()
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.save()
        form = ReviewForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {'product': product, 'form': form, 'category': category, 'categories': categories, 'products': products,
               'mycart_product_form': mycart_product_form}
    return render(request, 'cart/products/detail.html', context)
