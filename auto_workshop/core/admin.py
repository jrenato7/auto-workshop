from django.contrib import admin

from auto_workshop.core.models import Vehicle


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['plate', 'brand', 'model', 'color', 'year']


admin.site.register(Vehicle, VehicleModelAdmin)