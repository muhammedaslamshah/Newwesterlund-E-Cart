from django.db import models
from customers.models import Customer
from products.models import Product

# data Model for order
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    # Ordered Stages
    CART_STAGE=0
    # checkout 1st stage
    ORDER_CONFIRMED=1
    # for Admin (stages: 2,3,4 below)
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4 

    # Status Choices
    STATUS_CHOICE=((ORDER_CONFIRMED, "ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVER"),
                   (ORDER_REJECTED,"ORDER_REJECTED")
                   )
    
    # Show Status Feild  | at first time user create a cart / add item
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# Ordered item
class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

