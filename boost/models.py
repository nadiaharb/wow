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
    price=models.DecimalField(max_digits=6, decimal_places=2)
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
