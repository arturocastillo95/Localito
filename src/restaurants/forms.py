from django import forms
from .models import (
    Product, 
    Customer, 
    Order, 
    OrderItem,
    )

# class createCustomer(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['device']


# class createOrder(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['customer', 'restaurant']


# class addOrderItem(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['product','order', 'quantity']