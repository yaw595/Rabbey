from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Category, Product
from webstore.forms import (RegistrationForm, EditProfileForm, ChangePasswordForm, ResetPasswordForm)


# Create your views here.
def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'webstore/home.html', context)


def register(request):
    global args
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webstore')
    else:
        form = RegistrationForm()

        args = {'form': form}

    return render(request, 'webstore/reg_form.html', args)


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'base.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/webstore')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'webstore/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user, )

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/webstore/login')
        else:
            return redirect('/webstore/change_password')
    else:
        form = ChangePasswordForm(user=request.user)
        args = {'form': form}
        return render(request, 'webstore/change_password.html', args)


def reset_password(request):
    global args
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webstore/reset_password/done ')
    else:
        form = ResetPasswordForm()

        args = {'form': form}

    return render(request, 'webstore/reset_password.html', args)

