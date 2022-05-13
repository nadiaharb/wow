from django.urls import path
#from accounts import views as account_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('wow/services/', views.search, name='search'),
    path('wow/<slug:division_slug>/', views.division_details, name='division_details'),
    path('wow/services/<slug:service_name_slug>/', views.services, name='services'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='updateItem'),
    path('process_order/', views.process_order, name='process_order'),

    path('faqs/', views.faqs, name='faqs'),
    path('info/terms/', views.terms, name='terms'),
    path('info/privacy-policy/', views.privacy, name='privacy'),
    path('info/contact/', views.contact, name='contact'),



]