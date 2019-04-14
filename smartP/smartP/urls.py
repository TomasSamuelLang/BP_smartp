"""smartP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    path('contact/', contactpage, name='contact'),
    path('login/', loginpage, name='login'),
    path('register/', registerpage, name='register'),
    path('thanks/', thankspage, name="thanks"),
    path('home/<int:id>', parkingDetails, name="detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('favourite/', showFavourite, name='favourite'),
    path('addfav/<int:id>', add_favourite, name='addfav'),
    path('dislike/<int:id>', dislike, name='dislike'),
    path("filter/<int:id>/<str:date>", filtered_parking_details, name='filter'),
    path('location/lon=<str:longitude>&lat=<str:latitude>', location, name='location')
]
