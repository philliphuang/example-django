from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Cart_Item

"""displays checkout page with cart items for a user"""
def checkout(request):
    # TODO add if condition for if user exists
    shopping_cart = Customer.objects.get(user=request.user)
    cart_list = shopping_cart.cart.all()
    return render(request, 'cart/checkout.html', {'cart_list': cart_list})

"""adds given item to user's cart"""
def add_cart(request, pk):
    result = get_object_or_404(Cart_Item, pk=pk)
    shopping_cart = Customer.objects.get(user=request.user)
    shopping_cart.cart.add(result)
    return redirect(request.META['HTTP_REFERER'])

"""removes given item from user's cart"""
def remove_cart(request, pk):
    result = get_object_or_404(Cart_Item, pk=pk)
    shopping_cart = Customer.objects.get(user=request.user)
    shopping_cart.cart.remove(result)
    return redirect(request.META['HTTP_REFERER'])