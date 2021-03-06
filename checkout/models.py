from django.db import models
from products.models import Perfume 
# Create your models here.


class Customer(models.Model):
    """Customer object"""
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    street_address = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=10, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.first_name, self.last_name)



class OrderLineItem(models.Model):
    """Orderline object made with Customer and Perfume model combined"""
    order = models.ForeignKey(Customer, null=False)
    product = models.ForeignKey(Perfume, null=False)   
    quantity = models.IntegerField(blank=False)     

    def __str__(self):
        return "{0}-{1}@{2}".format(self.quantity, self.order.first_name, self.product.price)