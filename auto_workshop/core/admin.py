from django.contrib import admin
from django.db.models import Sum

from auto_workshop.core.models import Vehicle, Order, OrderPart, OrderLabor


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['plate', 'brand', 'model', 'color', 'year']


class PartInline(admin.TabularInline):
    readonly_fields = ['amount']
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
        resp = part_amount if part_amount else 0.0
        return format_currency(resp)

    part_amount.short_description = 'Total das peças'

    def labor_amount(self, obj):
        labor_amount = OrderLabor.objects.filter(order=obj).aggregate(
            Sum('price'))['price__sum']
        resp = labor_amount if labor_amount else 0.0
        return format_currency(resp)

    labor_amount.short_description = 'Total da mão de obra'

    def general_amount(self, obj):
        part_amount = float(self.part_amount(obj).replace("R$ ", ""))
        labor_amount = float(self.labor_amount(obj).replace("R$ ", ""))
        return format_currency(part_amount + labor_amount)

    general_amount.short_description = 'Total'


admin.site.register(Vehicle, VehicleModelAdmin)
admin.site.register(Order, OrderModelAdmin)


def format_currency(value):
    return "R$ %.2f" % value
