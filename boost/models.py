from django.contrib.auth.models import AbstractUser

from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils.text import slugify
# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    email=models.EmailField(default='')


    def __str__(self):
        return str(self.username)






class Division(models.Model):
    division=models.CharField(max_length=120)
    description=models.TextField()
    slug=models.SlugField(unique=True, blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.slug is None:
          self.slug=slugify(self.division)
          super().save( *args, **kwargs)

    def get_absolute_url(self):
        return reverse('division_details', kwargs={'division_slug':self.slug})

        #return f'/wow/{self.slug}'

    def __str__(self):
        return self.division


class Services(models.Model):
    division=models.ForeignKey(Division, on_delete=models.CASCADE)
    service_name=models.CharField(max_length=120)
    description=models.TextField()
    price=models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    image=models.ImageField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.slug is None:
           self.slug=slugify(self.service_name)
           super().save( *args, **kwargs)



    def get_absolute_url(self):
        return reverse('services', kwargs={'service_name_slug':self.slug})



    def __str__(self):
        return self.service_name


class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    paid= models.BooleanField(default=False, null=True, blank=False)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)



    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return int(total)











class OrderItem(models.Model):
    service=models.ForeignKey(Services, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service.service_name


    @property
    def get_total(self):
        total=self.service.price*self.quantity
        return total
