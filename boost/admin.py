from django.contrib import admin

from boost.models import User, Division, Services,Order, Customer, OrderItem
# Register your models here.




admin.site.register(User)
admin.site.register(Division)
admin.site.register(Services)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderItem)