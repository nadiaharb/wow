from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from .utils import cookieCart, guestOrder, cartData
# Create your views here.

def index(request):
    divisions=Division.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    context={'divisions':divisions, 'cartItems':cartItems}
    return render(request, 'boost/home.html', context)







def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "boost/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "boost/login.html")

def logout_view(request):

        logout(request)

        return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "boost/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "boost/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "boost/register.html")





def division_details(request, division_slug):

    div_object=Division.objects.get(slug=division_slug)
    services=Services.objects.filter(division=div_object)
    data = cartData(request)
    cartItems = data['cartItems']

    context={'div_object':div_object, 'services':services, 'cartItems':cartItems}

    return render(request, 'boost/div_details.html', context=context)

def services(request, service_name_slug):

    service_object=Services.objects.get(slug=service_name_slug)

    data = cartData(request)
    cartItems = data['cartItems']
    context = {'service_object': service_object, 'cartItems':cartItems}
    return render(request, 'boost/service_details.html', context=context)


def search(request):
    query=request.GET.get('q')
    services=Services.objects.all()
    if query is not None:
        lookups=Q(service_name__icontains=query) | Q(description__icontains=query)
        services=Services.objects.filter(lookups)
    context={'services':services}
    return render(request, 'boost/search.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']


    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'boost/cart.html', context)


def checkout(request):
    data=cartData(request)
    cartItems=data['cartItems']
    items = data['items']
    order = data['order']
    context={'items':items, 'order':order, 'cartItems':cartItems}

    return render(request, 'boost/checkout.html', context)


@csrf_exempt
def updateItem(request):
    data=json.loads(request.body)
    service_name=data['service']
    action=data['action']
    customer=request.user.customer
    service=Services.objects.get(service_name=service_name)
    order, created = Order.objects.get_or_create(customer=customer, paid=False)
    orderItem, created=OrderItem.objects.get_or_create(order=order, service=service)
    if action=='add':
        orderItem.quantity+=1
    elif action=='remove':
        orderItem.quantity-=1
    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('Added', safe=False)






@csrf_exempt
def process_order(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:

        customer=Customer.objects.get(user=request.user)

        order, created = Order.objects.get_or_create(customer=customer, paid=False)

    else:
        customer, order=guestOrder(request, data)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    print('TOTAL ', total, type(total))
    print('CART ' ,order.get_cart_total, type(order.get_cart_total))
    if total == order.get_cart_total:
        print(total == order.get_cart_total)
        order.paid = True
    order.save()
    return JsonResponse('Payment complete', safe=False)

def faqs(request):
    return render(request, 'boost/faq.html')

def terms(request):
    return render(request, 'boost/terms.html')


def privacy(request):
    return render(request, 'boost/privacy.html')

def ex(request):
    return render(request, 'boost/ex.html')