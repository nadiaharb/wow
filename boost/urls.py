from django.urls import path
#from accounts import views as account_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('wow/services/', views.search, name='search'),
    path('wow/<slug:division_slug>/', views.division_details, name='division_details'),
    path('wow/services/<slug:service_name_slug>/', views.services, name='services'),


]