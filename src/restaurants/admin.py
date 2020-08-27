from django.contrib import admin
from .models import ( 
    Restaurant,
    Section,
    Product,
    Customer,
    Order,
    OrderItem,
    )

admin.site.register(Restaurant)
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

