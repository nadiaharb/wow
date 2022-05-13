import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print(cart)
    cartItems = 0
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            service = Services.objects.get(service_name=i)
            total = (service.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            item = {
                'service': {
                    'service_name': service.service_name,
                    'price': service.price,
                    'image': service.image

                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
        except:
            pass

    return {'cartItems':cartItems, 'order':order, 'items':items}





def guestOrder(request, data):
    print(request.COOKIES)
    username = data['form']['username']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']
    customer, created = Customer.objects.get_or_create(
        email=email
    )
    customer.username = username
    customer.save()
    order = Order.objects.create(customer=customer, paid=False)
    for item in items:
        service = Services.objects.get(service_name=item['service']['service_name'])
        orderItem = OrderItem.objects.create(service=service, order=order, quantity=item['quantity'])

    return customer, order

def cartData(request):
    if request.user.is_authenticated:
        user=request.user
        customer, created=Customer.objects.get_or_create(user=user, username=user)
        print( customer)
        order,created=Order.objects.get_or_create(customer=customer, paid=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
        print(order, 'user utils')
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        print(items, 'guest utils')
    return {'cartItems':cartItems, 'order':order, 'items':items}
