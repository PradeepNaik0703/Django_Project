from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=False)
    email = models.EmailField(default=None, max_length=200,null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200,null=False)
    price = models.FloatField()
    digital = models.BooleanField(default=False,blank=False)
    images = models.ImageField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    @property
    def ImageUrl(self):
        try:
            url = self.images.url
        except :
            url = ''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=False)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def get_total_cost(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.TotalCost for item in orderitem])
        return total
    
    @property
    def get_total_item(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def TotalCost(self):
        return self.quantity * self.product.price
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    zipcode = models.IntegerField(max_length=6,null=False)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.address




