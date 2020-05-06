from django.contrib import admin
from .models import *


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'type', 'property_state']

admin.site.register(ApartmentType)
admin.site.register(Apartment, ApartmentAdmin)
