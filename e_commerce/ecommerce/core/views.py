from django.shortcuts import render
from .models import *
# Create your views here.

def store_veiw(request):
    product = Product.objects.all()
    context ={'pd':product}
    return render(request,'core/store.html',context)


def cart_view(request):
    if request.user.is_authenticated:
        cust = request.user.customer
        print(cust)
        order , create = Order.objects.get_or_create(customer=cust,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_cost' : 0 , 'get_total_item' : 0}
    context ={'items':items,'order':order}
    return render(request,'core/cart.html',context)

def checkout_view(request):
    if request.user.is_authenticated:
        cust = request.user.customer
        print(cust)
        order , create = Order.objects.get_or_create(customer=cust,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_cost' : 0 , 'get_total_item' : 0}
    context ={'items':items,'order':order}
    return render(request,'core/checkout.html',context)