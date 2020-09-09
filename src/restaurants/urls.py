from django.urls import path

from restaurants.views import (
    newItemOrderView,
    updateOrderView,
    setOrderView,
    cartView,
    addDeliveryView,
    removeDeliveryView,
    lastStepFormView,
    addDeliveryDetailsView,
)

urlpatterns = [
    path('ajax/newitemorder', newItemOrderView, name='newItemOrder'),
    path('ajax/updateorder', updateOrderView, name='updateOrder'),
    path('ajax/setorder', setOrderView, name='setOrder'),
    path('ajax/add-delivery', addDeliveryView, name='addDelivery'),
    path('ajax/remove-delivery', removeDeliveryView, name='removeDelivery'),
    path('ajax/add-delivery-details', addDeliveryDetailsView, name='addDeliveryDetails'),
]