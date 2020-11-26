from django.urls import path
from .views import dashboardView, getModalURL, qrDownloadView, restaurantInfoView, catalogEditView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('<str:restaurant>/qr-code', qrDownloadView, name='qrDownload'),
    path('<str:restaurant>/editar-informacion', restaurantInfoView, name='restaurantInfo'),
    path('<str:restaurant>/editar-productos', catalogEditView, name='catalogEdit'),
    path('ajax/modalurls', getModalURL, name='getModalURL'),
]