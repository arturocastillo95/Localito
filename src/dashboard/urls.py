from django.urls import path
from .views import dashboardView, getModalURL, qrDownloadView, restaurantInfoView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('<str:restaurant>/qr-code', qrDownloadView, name='qrDownload'),
    path('<str:restaurant>/editar-informacion', restaurantInfoView, name='restaurantInfo'),
    path('ajax/modalurls', getModalURL, name='getModalURL'),
]