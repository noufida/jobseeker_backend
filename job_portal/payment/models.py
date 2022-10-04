
from django.db import models
from user.models import Account
# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    valid_days = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    # plan = models.ForeignKey(Plan,on_delete=models.CASCADE,null=True,blank=True)
    order_product = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_product

