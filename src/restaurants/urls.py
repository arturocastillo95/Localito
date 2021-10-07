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
    order_success_view
)

urlpatterns = [
    path('newitemorder', newItemOrderView, name='newItemOrder'),
    path('updateorder', updateOrderView, name='updateOrder'),
    path('setorder', setOrderView, name='setOrder'),
    path('add-delivery', addDeliveryView, name='addDelivery'),
    path('remove-delivery', removeDeliveryView, name='removeDelivery'),
    path('add-delivery-details', addDeliveryDetailsView, name='addDeliveryDetails'),
    path('order-success', order_success_view, name='order-success')
]