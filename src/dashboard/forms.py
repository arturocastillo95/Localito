from django import forms
from restaurants.models import Restaurant

class RestaurantInfoForm(forms.ModelForm):
    name = forms.CharField(label="Nombre de tienda", widget=forms.TextInput(attrs={'class':'input'}))
    address = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class':'input'}))

    class Meta:
        model = Restaurant
        fields = ['name', 'address']