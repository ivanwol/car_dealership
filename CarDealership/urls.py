"""CarDealership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from user import views as user_view
from car import views as car_views
from dealer import views as dealer_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_view.user),
    path('login/', user_view.login),
    path('logout/', user_view.logout),
    path('registration/', user_view.registration),

    path('car/', car_views.car),
    path('car/create/<id>', car_views.create),
    path('car/info/<id>', car_views.info),
    path('car/<id>', car_views.id_car),

    path('dealer/name/<id>', dealer_views.name),
    path('dealer/<id>', dealer_views.name),
    path('dealer/', dealer_views.name_dealer),
]
