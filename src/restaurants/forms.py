from django import forms
from .models import (
    Restaurant,
    Product, 
    Customer, 
    Order, 
    OrderItem,
    )

from phonenumber_field.formfields import PhoneNumberField

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

class submitOrderForm(forms.ModelForm):
    name = forms.CharField(max_length=60, label='Nombre', widget=forms.TextInput(attrs={'class':'input','autocomplete':'name'}))
    address = forms.CharField(max_length=60, label='Dirección de Entrega', widget=forms.TextInput(attrs={'class':'input','autocomplete':'address'}))
    email = forms.EmailField(max_length=60, label='Correo Electronico (Opcional)', widget=forms.EmailInput(attrs={'class':'input','autocomplete':'email'}), required=False)
    phone = PhoneNumberField(label='Número de WhatsApp', widget=forms.EmailInput(attrs={'class':'input','autocomplete':'tel'}))

    class Meta:
        model = Customer
        fields = ['name', 'address', 'email']

class orderNotesForm(forms.ModelForm):
    notes = forms.CharField(label='Agregar notas para mi orden', widget=forms.Textarea(attrs={'class':'textarea', 'rows':'2'}), required=False)
    class Meta:
        model = Order
        fields = ['notes']

