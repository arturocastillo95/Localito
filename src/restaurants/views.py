from django.shortcuts import render, redirect
from .models import (
    Restaurant,
    Section,
    Product,
    Customer,
    OrderItem,
    Order,
    )
from localito.settings import STATIC_DIR
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.

def restaurantView(request, restaurant):
    try:
        restaurant = Restaurant.objects.get(slug=restaurant)
        context = {
            'name': restaurant.name,
            'slug': restaurant.slug,
            'social_links': restaurant.get_social_links(),
            'address': restaurant.get_full_address(),
            'business_hours': restaurant.business_hours,
            'about': restaurant.about,
            'currency': restaurant.get_currency_display(),
        }
        if restaurant.image:
            context['image'] = restaurant.image.url

        try:
            sections = Section.objects.filter(restaurant=restaurant)
            sections = sections.order_by('order')
            catalog = {}

            for section in sections:
                product_list = {}
                try:
                    products = Product.objects.filter(section=section)
                    for product in products:
                        product_list[product.name] = [product.description, product.price, product.id]
                        if product.image:
                            product_list[product.name].append(product.image.url)
                    catalog[section.name] = product_list
                except Product.DoesNotExist:
                    pass

            context['catalog'] = catalog

        except Section.DoesNotExist:
            pass

        return render(request, 'restaurants/restaurant.html', context)
    
    except Restaurant.DoesNotExist:
        return redirect('home')

def newItemOrderView(request):
    itemOrderId = request.POST.get('itemOrderId')
    store = request.POST.get('store')
    device = request.POST.get('device')
    product = Product.objects.get(id=itemOrderId)

    if request.POST:
        customer, created = Customer.objects.get_or_create(device=device)
        restaurant = Restaurant.objects.get(slug=store)

        try:
            order = Order.objects.get(customer=customer, restaurant=restaurant, complete=False)
        except Order.DoesNotExist:
            order = Order.objects.create(customer=customer, restaurant=restaurant)
        
        try:
            orderItem = OrderItem.objects.get(product=product, order=order)
            orderItem.quantity = 1
            orderItem.save()
        except OrderItem.DoesNotExist:
            orderItem = OrderItem.objects.create(product=product, order=order, quantity=1)

        return JsonResponse({'total': order.get_cart_total, 'item_sum': order.get_cart_items}, status=200)

def updateOrderView(request):

    if request.GET:
        itemId = request.GET.get('product')
        store = request.GET.get('store')
        device = request.GET.get('device')

        product = Product.objects.get(id=itemId)
        customer = Customer.objects.get(device=device)
        order = Order.objects.get(customer=customer)
        item = OrderItem.objects.get(product=product, order=order)

        response = JsonResponse({'quantity': item.quantity}, status=200)

        return response
    
    if request.POST:
        itemId = request.POST.get('product')
        store = request.POST.get('store')
        device = request.POST.get('device')
        opertation = request.POST.get('operation')

        restaurant = Restaurant.objects.get(slug=store)
        product = Product.objects.get(id=itemId)
        customer = Customer.objects.get(device=device)
        order = Order.objects.get(customer=customer, restaurant=restaurant, complete=False)
        item = OrderItem.objects.get(product=product, order=order)

        if opertation == 'add':
            item.quantity += 1
            item.save()
        else:
            if item.quantity > 0:
                item.quantity += -1
                item.save()

        response = JsonResponse({'quantity': item.quantity, 'total': order.get_cart_total, 'item_sum': order.get_cart_items}, status=200)

        return response
        

def setOrderView(request):
    if request.GET:
        device = request.COOKIES.get('device')
        store = request.GET.get('store')

        try:
            customer = Customer.objects.get(device=device)
            try:
                restaurant = Restaurant.objects.get(slug=store)
                order = Order.objects.get(customer=customer, restaurant=restaurant)

                if not order.complete:
                    all_products = order.get_order_products
                    all_list = {}

                    for product in all_products:
                        all_list[product.product.id] = product.quantity

                    return JsonResponse({'user_exist': True, 'order_exist': True, 'products_set': all_list, 'total': order.get_cart_total, 'item_sum': order.get_cart_items}, status=200)
                else:
                    return JsonResponse({'user_exist': True, 'order_exist': False}, status=200)

            except Order.DoesNotExist:
                return JsonResponse({'user_exist': True, 'order_exist': False}, status=200)

        except Customer.DoesNotExist:
            return JsonResponse({'user_exist': False, 'order_exist': False}, status=200)


        





