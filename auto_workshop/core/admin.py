from django.contrib import admin
from django.db.models import Sum

from auto_workshop.core.models import Vehicle, Order, OrderPart, OrderLabor


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['plate', 'brand', 'model', 'color', 'year']


class PartInline(admin.TabularInline):
    model = OrderPart
    extra = 1


class LaborInline(admin.TabularInline):
    model = OrderLabor
    extra = 1


class OrderModelAdmin(admin.ModelAdmin):
    inlines = [PartInline, LaborInline]
    list_display = ['vehicle', 'date', 'part_amount', 'labor_amount',
                    'general_amount']

    def part_amount(self, obj):
        part_amount = OrderPart.objects.filter(order=obj).aggregate(
            Sum('amount'))['amount__sum']
        return part_amount if part_amount else 0

    part_amount.short_description = 'Total das peças'

    def labor_amount(self, obj):
        labor_amount = OrderLabor.objects.filter(order=obj).aggregate(
            Sum('price'))['price__sum']
        return labor_amount if labor_amount else 0

    labor_amount.short_description = 'Total da mão de obra'

    def general_amount(self, obj):
        return self.part_amount(obj) + self.labor_amount(obj)

    general_amount.short_description = 'Total'


admin.site.register(Vehicle, VehicleModelAdmin)
admin.site.register(Order, OrderModelAdmin)
