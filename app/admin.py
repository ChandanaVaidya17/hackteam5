from django.contrib import admin
from . import models
from .models import City
# Register your models here.
class CityAdmin(admin.AdminSite):
    site_header = 'City admin areas'

city_site=CityAdmin(name='CityAdmin')

city_site.register(City)