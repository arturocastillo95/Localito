from django.db import models
from account.models import Account
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from .symbols import symbols
import urllib.parse
import pyqrcode
from PIL import Image
from django.urls import reverse
from io import BytesIO
from django.contrib.sites.shortcuts import get_current_site
from django.core.files import File
import os



class Restaurant(models.Model):
    owner                   = models.ForeignKey(Account, default=None, on_delete=models.CASCADE, blank=True)
    name                    = models.CharField(max_length=60)
    slug                    = models.SlugField(unique=True, blank=True)
    address                 = models.CharField(max_length=80, blank=True)
    currency                = models.CharField(choices=symbols, max_length=30, default='USD')
    city                    = models.CharField(max_length=60, blank=True)
    country                 = models.CharField(max_length=60, blank=True)
    postal_code             = models.CharField(max_length=60, blank=True)
    business_hours          = models.CharField(max_length=30, blank=True)
    image                   = models.ImageField(upload_to='restaurant-images', verbose_name='Logo de Restaurante', blank=True)
    about                   = models.TextField(max_length=300, blank=True)
    delivery_price          = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    whatsapp_number         = PhoneNumberField(blank=True)
    facebook_url            = models.URLField(max_length=60, blank=True, verbose_name="Link de Facebook")
    instagram_url           = models.URLField(max_length=60, blank=True, verbose_name="Link de Instagram")
    qr_code                 = models.ImageField(upload_to='qr-codes', verbose_name='Código QR', blank=True, null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            url = self.qr_code.url
            image_path = urlparse(url)
            file_name = os.path.basename(image_path.path)

            if self.slug not in file_name:
                raise Exception()

        except:
            memfile = BytesIO()

            qr = pyqrcode.QRCode(self.storeURL)
            qr.png(memfile, scale=10)
            self.qr_code.save(self.slug + '.png', File(memfile), save=False)
            super(Restaurant, self).save(*args, **kwargs)
            memfile.close()


    def get_social_links(self):
        links = {}
        if self.facebook_url:
            links['fa-facebook-f'] = self.facebook_url
        if self.instagram_url:
            links['fa-instagram'] = self.instagram_url
        return links
    
    @property
    def get_full_address(self):
        address = ''
        if self.address:
            address += self.address
        if self.city:
            address += ', ' + self.city
        if self.country:
            address += ', ' + self.country
        return address
    
    @property
    def imageURL(self):
        try:
            url = self.image.url    
        except:
            url = False
        return url
    
    @property
    def storeURL(self):
        request = None
        domain = get_current_site(request).domain
        url = 'http://' + domain + reverse('restaurant', args=(self.slug,))
        print(url)
        return url



class Section(models.Model):
    restaurant              = models.ForeignKey(Restaurant, default=None, on_delete=models.CASCADE, blank=True)
    name                    = models.CharField(max_length=20, blank=True)
    description             = models.TextField(max_length=300, blank=True)
    order                   = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' - ' + self.restaurant.name

class Product(models.Model):
    section                 = models.ForeignKey(Section, default=None, on_delete=models.CASCADE, blank=True)
    name                    = models.CharField(max_length=60, blank=True)
    description             = models.TextField(max_length=150, blank=True)
    image                   = models.ImageField(upload_to='products', blank=True)
    price                   = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name + ' - ' + self.section.name + ' - ' + self.section.restaurant.name

class Customer(models.Model):
    user                    = models.OneToOneField(Account, null=True, blank=True, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=200, null=True)
    email                   = models.EmailField(max_length=60)
    address                 = models.CharField(max_length=200, null=True, blank=True)
    device                  = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.device

class Order(models.Model):
    customer                = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True, null=True)
    restaurant              = models.ForeignKey(Restaurant,on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered            = models.DateTimeField(auto_now_add=True)
    complete                = models.BooleanField(default=False)
    is_delivery             = models.BooleanField(default=True, null=True, blank=True)
    notes                   = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderItems          = self.orderitem_set.all()
        total               = sum([item.get_total for item in orderItems])
        return total
    
    @property
    def get_order_products(self):
        orderItems = self.orderitem_set.all()
        return orderItems

    @property 
    def get_cart_items(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total
    
    @property
    def whatsapp_link(self):
        total = self.get_cart_total
        delivery_price = self.restaurant.delivery_price
        restaurant_name = self.restaurant.name
        client_name = self.customer.name
        client_address = self.customer.address

        all_products = self.get_order_products
        product_list = ""

        for item in all_products:
            quantity = item.quantity
            if quantity > 0:
                item_name = '\n' + '-' + str(quantity) + ' x ' + item.product.name + ' (' + str(item.get_total) + ')'
                product_list += item_name
                
        if self.is_delivery and delivery_price > 0:
            total += self.restaurant.delivery_price
            product_list += '\n' + '-Envío a domocilio' + ' (' + str(delivery_price) + ')'

        message = f"Hola {restaurant_name} soy *{client_name}* y quiero hacer un pedido para la dirección *{client_address}*:\n{product_list}\n\n*Total: {total}*\n\n¡Gracias!"
        encoded_message = urllib.parse.quote(message)
        phone = str(self.restaurant.whatsapp_number).replace('+','')

        return "https://wa.me/" + phone + "?text=" + encoded_message



class OrderItem(models.Model):
    product                 = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order                   = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity                = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    






