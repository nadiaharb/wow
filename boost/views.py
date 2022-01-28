from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Division, Services,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    divisions=Division.objects.all()
    return render(request, 'boost/home.html', {'divisions':divisions})







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
    context={'div_object':div_object, 'services':services}

    return render(request, 'boost/div_details.html', context=context)

def services(request, service_name_slug):

    service_object=Services.objects.get(slug=service_name_slug)
    context={'service_object':service_object}
    return render(request, 'boost/service_details.html', context=context)


def search(request):
    query=request.GET.get('q')
    services=Services.objects.all()
    if query is not None:
        lookups=Q(service_name__icontains=query) | Q(description__icontains=query)
        services=Services.objects.filter(lookups)
    context={'services':services}
    return render(request, 'boost/search.html', context)

