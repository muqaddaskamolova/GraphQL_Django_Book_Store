from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from book.models import Books

from .cart import Cart


def basket_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html', {'cart': cart})


def basket_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Books, id=product_id)
        cart.add(product=product, qty=product_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        return response


def basket_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

        cartqty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': cart_total})
        return response


def basket_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        cartqty = cart.__len__()
        basketsubtotal = cart.get_subtotal_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': basketsubtotal})
        return response
