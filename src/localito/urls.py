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
from django.urls import path, include

from restaurants.views import (
    restaurantView,
    cartView,
    lastStepFormView,
)
from pagemanager.views import homeScreenView
from dashboard.views import dashboardView
from account.views import registerView, logoutView, loginView

#Images config
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboardView, name='dashboard'),
    path('', homeScreenView, name="home"),
    path('registro/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('acceder/', loginView, name='login'),
    path('<str:restaurant>/', restaurantView, name='restaurant'),
    path('<str:restaurant>/cart/', cartView, name='cart'),
    path('<str:restaurant>/checkout/id=<int:orderId>', lastStepFormView, name='checkout'),
    path('ajax/', include('restaurants.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)