from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from django.contrib.auth.decorators import login_required
from localito.custom_decorators import ajax_required
from django.urls import reverse
from django.http import JsonResponse



@login_required
def dashboardView(request):
    if request.user.is_authenticated:
        context = {}
        restaurant_dict = {}
        restaurants = Restaurant.objects.filter(owner=request.user)

        for restaurant in restaurants:
            restaurant_dict[restaurant.name] = [restaurant.imageURL, restaurant.get_full_address, restaurant.slug]
        
        context['restaurants'] = restaurant_dict
        return render(request, 'dashboard/negocios.html', context)
    else:
        return redirect('home')

@ajax_required
def getModalURL(request):
    if request.GET:
        store_slug = request.GET.get('store')
        store_url = reverse('restaurant', args=(store_slug,))
        share_url = request.build_absolute_uri(store_url)
        qr_url = reverse('qrDownload', args=(store_slug,))
        return JsonResponse({'store_URL': store_url, 'share_URL': share_url, 'qr_URL': qr_url}, status=200)

@login_required
def qrDownloadView(request, slug):
    restaurant = Restaurant.objects.get(slug=slug)
    context = {
        'qr_url': restaurant.qr_code.url,
        'store_name': restaurant.name,
        }
    return render(request, 'dashboard/qr_download.html', context)

