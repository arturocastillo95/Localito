from django.urls import path
from .views import dashboardView, getModalURL, qrDownloadView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('<str:restaurant>/qr-code', qrDownloadView, name='qrDownload'),
    path('ajax/modalurls', getModalURL, name='getModalURL'),
]