from django.contrib import admin
from .models import *


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'type', 'property_state']
    exclude = ['owner']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user.profile
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        if not request.user.is_superuser:
            qs = Apartment.objects.filter(owner=request.user.profile)
        else:
            qs = Apartment.objects.all()
        return qs


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'content']


admin.site.register(ApartmentType)
admin.site.register(Apartment, ApartmentAdmin)
