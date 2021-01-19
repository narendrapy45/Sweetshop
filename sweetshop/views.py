from django.shortcuts import render,redirect
from django.contrib import messages,auth
from products.models import ProductModel
from carts.utils import cartData
def homeView(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = ProductModel.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'home.html',context)