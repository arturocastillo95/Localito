from django.shortcuts import render, redirect
from restaurants.models import Restaurant, Section, Product
from django.contrib.auth.decorators import login_required
from localito.custom_decorators import ajax_required, must_be_owner
from django.urls import reverse
from django.http import JsonResponse
from .forms import RestaurantInfoForm



@login_required
def dashboardView(request):
    context = {}
    restaurant_dict = {}
    restaurants = Restaurant.objects.filter(owner=request.user)

    for restaurant in restaurants:
        restaurant_dict[restaurant.name] = [restaurant.imageURL, restaurant.get_full_address, restaurant.slug]
    
    context['restaurants'] = restaurant_dict
    return render(request, 'dashboard/negocios.html', context)


@ajax_required
def getModalURL(request):
    if request.GET:
        store_slug = request.GET.get('store')
        store_url = reverse('restaurant', args=(store_slug,))
        share_url = request.build_absolute_uri(store_url)
        qr_url = reverse('qrDownload', args=(store_slug,))
        info_url = reverse('restaurantInfo', args=(store_slug,))
        edit_url = reverse('catalogEdit', args=(store_slug,))
        return JsonResponse({'store_URL': store_url, 'share_URL': share_url, 'qr_URL': qr_url, 'info_URL': info_url, 'edit_URL': edit_url }, status=200)

@login_required
@must_be_owner
def qrDownloadView(request, restaurant):
    restaurant = Restaurant.objects.get(slug=restaurant)
    context = {
        'qr_url': restaurant.qr_code.url,
        'store_name': restaurant.name,
        }
    return render(request, 'dashboard/qr_download.html', context)

@login_required
@must_be_owner
def restaurantInfoView(request, restaurant):
    context = {}
    restaurant = Restaurant.objects.get(slug=restaurant)
    if request.POST:
        form = RestaurantInfoForm(request.POST, request.FILES)
        form.instance = restaurant
        if form.is_valid:
            form.save()
            return redirect('dashboard')
        else:
            context = {
                'info_form': form,
            }
    else:
        form = RestaurantInfoForm(
            initial = {
                'name': restaurant.name,
                'address': restaurant.address,
                'city': restaurant.city,
                'store_country': restaurant.store_country.code,
            }
        )
    context = {
        'info_form': form,
        'store_name': restaurant.name,
        'store_image': restaurant.imageURL,
    }
    return render(request, 'dashboard/restaurant_info.html', context)


@login_required
@must_be_owner
def catalogEditView(request, restaurant):
    restaurant = Restaurant.objects.get(slug=restaurant)
    context = {
        'store_name': restaurant.name,
        }

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


    return render(request, 'dashboard/catalog_edit.html', context)
