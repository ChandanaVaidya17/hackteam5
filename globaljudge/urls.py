"""globaljudge URL Configuration

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
from app import views
from app.admin import city_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin1/',city_site.urls),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home1/', views.HomePages, name='home1'),
    path('city/', views.City, name='city'),
    path('petra/', views.Petra, name='petra'),
    path('statue/', views.Statue, name='statue'),
    path('machu/', views.Machu, name='machu'),
    path('chicken/', views.Chicken, name='chicken'),
    path('roman/', views.Roman, name='roman'),
    path('tajmahal/', views.TajMahal, name='tajmahal'),
    path('',views.HomePage,name='home'),
    path('search/',views.search,name='search'),
    path('logout/', views.LogoutPage, name='logout'),
    path('search/', views.search, name='tajmahal'),
]
