from django.contrib import admin
from .models import *


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'type', 'property_state']
    exclude = ['owner', 'comments']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user.profile
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = Apartment.objects.filter(owner=request.user.profile)
        return qs


admin.site.register(ApartmentType)
admin.site.register(Apartment, ApartmentAdmin)
