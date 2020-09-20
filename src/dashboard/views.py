from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from django.contrib.auth.decorators import login_required


@login_required
def dashboardView(request):
    if request.user.is_authenticated:
        context = {}
        restaurant_dict = {}
        restaurants = Restaurant.objects.filter(owner=request.user)

        for restaurant in restaurants:
            restaurant_dict[restaurant.name] = [restaurant.imageURL, restaurant.get_full_address]
        
        context['restaurants'] = restaurant_dict
        return render(request, 'dashboard/negocios.html', context)
    else:
        return redirect('home')
