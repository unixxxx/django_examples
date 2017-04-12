from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from cart.cart import Cart

from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST or None)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])  
        cart.clear()
        order_created.delay(order.id)
        request.session['order_id'] = order.id # redirect to the payment
        return redirect(reverse('payment:process'))
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
