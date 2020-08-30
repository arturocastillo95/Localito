"""localito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from restaurants.views import (
    restaurantView,
    newItemOrderView,
    updateOrderView,
    setOrderView,
    cartView,
    addDeliveryView,
    removeDeliveryView,
    lastStepFormView,
)

from pagemanager.views import homeScreenView

#Images config
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeScreenView, name="home"),
    path('<str:restaurant>/', restaurantView, name='restaurant'),
    path('ajax/newitemorder', newItemOrderView, name='newItemOrder'),
    path('ajax/updateorder', updateOrderView, name='updateOrder'),
    path('ajax/setorder', setOrderView, name='setOrder'),
    path('ajax/add-delivery', addDeliveryView, name='addDelivery'),
    path('ajax/remove-delivery', removeDeliveryView, name='removeDelivery'),
    path('<str:restaurant>/cart/', cartView, name='cart'),
    path('<str:restaurant>/checkout/id=<int:orderId>', lastStepFormView, name='checkout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)