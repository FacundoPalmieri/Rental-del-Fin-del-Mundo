from django.contrib import admin
from .models import *
from django.urls import reverse
import json
from .forms import *
from decimal import Decimal, ROUND_HALF_UP
class PlanAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'trimestre', 'un_dia', 'dos_a_tres', 'cuatro_a_seis', 'siete_o_mas', 'hora_extra']
    readonly_fields = ['dos_a_tres', 'cuatro_a_seis', 'siete_o_mas']

    def dos_a_tres(self, obj):
        return self._round_decimal(obj.un_dia * (Decimal('1') - Decimal(str(obj.discount_percentages[obj.tipo]['dos_a_tres'])) / Decimal('100')))

    def cuatro_a_seis(self, obj):
        return self._round_decimal(obj.un_dia * (Decimal('1') - Decimal(str(obj.discount_percentages[obj.tipo]['cuatro_a_seis'])) / Decimal('100')))

    def siete_o_mas(self, obj):
        return self._round_decimal(obj.un_dia * (Decimal('1') - Decimal(str(obj.discount_percentages[obj.tipo]['siete_o_mas'])) / Decimal('100')))

    def _round_decimal(self, value):
        # Round the value to the nearest integer
        rounded_value = round(Decimal(value))
        # If the rounded value is 0, set it to the original value
        if rounded_value == 0:
            rounded_value = value
        # Format the rounded value with commas and three zero decimals
        formatted_value = f"{rounded_value:,.0f},000"
        return formatted_value


admin.site.register(Plan, PlanAdmin)

admin.site.register(Auto)
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    form = RentalForm
    change_list_template = 'admin/rental_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request, extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        # Customize this according to your Rental model
        rentals_data = [{'title': f"{rental.auto} / {rental.nombre} {rental.apellido}",
                        'start': rental.fecha_retiro.strftime('%Y-%m-%d'),
                        'end': rental.fecha_devolucion.strftime('%Y-%m-%d') if rental.fecha_devolucion else None,
                        'url': reverse('admin:rental_rental_change', args=(rental.pk,)),
                        'color': rental.color}  # Include color information
                        for rental in qs]

        response.context_data['rentals_json'] = json.dumps(rentals_data)

        return response
