from django.contrib import admin
from .models import *
from django.urls import reverse
import json
from .forms import *
from decimal import Decimal, ROUND_HALF_UP
from django.utils.html import format_html
import math
class PlanAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    readonly_fields = ['descuentos']

    def descuentos(self, obj):
        discount_percentages = {
            'Basico': {'dos_a_tres': Decimal('6.69'), 
                       'cuatro_a_seis': Decimal('9.26'), 
                       'siete_o_mas': Decimal('10.82'), 
                       #'hora_extra': Decimal('91.02')
                       },
            'Estandar': {'dos_a_tres': Decimal('6.98'), 
                         'cuatro_a_seis': Decimal('8.30'), 
                         'siete_o_mas': Decimal('11.63'), 
                         #'hora_extra': Decimal('91.02')
                         },
            'Pro': {'dos_a_tres': Decimal('4.55'), 
                    'cuatro_a_seis': Decimal('7.06'), 
                    'siete_o_mas': Decimal('7.58'), 
                    #'hora_extra': Decimal('91.02')
                    }
        }

        discount_descriptions = {
            'dos_a_tres': 'dos a tres días',
            'cuatro_a_seis': 'cuatro a seis días',
            'siete_o_mas': 'siete o más días',
            'hora_extra': 'hora extra',
        }

        # Initialize a dictionary to store the discounted prices for each month
        discounted_prices_dict = {}

#ROUND UP
        # Loop through each month and calculate the discounted prices
        for month in Plan._meta.get_fields():
            if month.name in ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']:
                month_name = month.name
                un_discounted_price = getattr(obj, month_name)
                discounts_str = ''
                for discount_type, percentage in discount_percentages[obj.tipo].items():
                    discount_description = discount_descriptions.get(discount_type, discount_type)
                    #Si es hora extra redondeo con decimal, ejemplo 3.500, si no redondeo a 4.000 o 3.000
#                    if discount_type == 'hora_extra':
#                        discounted_price = un_discounted_price * (1 - percentage / Decimal('100'))
#                        discounted_price = math.ceil(discounted_price * 1000) / 1000
#                        discounted_price = round(discounted_price, 1)
#                        discounted_price = f"${discounted_price}00"
#                    else:
                    discounted_price = f"${math.ceil(un_discounted_price * (1 - percentage / Decimal('100')))}.000"
                    discounts_str += f"{discount_description}: {discounted_price}<br>"
                discounted_prices_dict[month_name] = discounts_str

        # Format the discounted prices as HTML
        discounted_prices_html = ''
        for month, discounts in discounted_prices_dict.items():
            discounted_prices_html += f"{month}:<br>{discounts}<br>"

        return format_html(discounted_prices_html)

#        for month in Plan._meta.get_fields():
#            if month.name in ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']:
#                month_name = month.name
#                un_discounted_price = getattr(obj, month_name)
#                discounts_str = ''
#                for discount_type, percentage in discount_percentages[obj.tipo].items():
#                    discounted_price = f"${round(un_discounted_price * (1 - percentage / Decimal('100')))}.000"
#                    discount_description = discount_descriptions.get(discount_type, discount_type)
#                    discounts_str += f"{discount_description}: {discounted_price}<br>"
#                discounted_prices_dict[month_name] = discounts_str

        # Format the discounted prices as HTML
#        discounted_prices_html = ''
#        for month, discounts in discounted_prices_dict.items():
#            discounted_prices_html += f"{month}:<br>{discounts}<br>"

#        return format_html(discounted_prices_html)

    # Set the description for the column
    descuentos.short_description = 'Descuentos'
    # Allow HTML tags in the column
    descuentos.allow_tags = True
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
                        'start': rental.fecha_retiro.strftime('%Y-%d-%m'),
                        'end': rental.fecha_devolucion.strftime('%Y-%d-%m') if rental.fecha_devolucion else None,
                        'url': reverse('admin:rental_rental_change', args=(rental.pk,)),
                        'color': rental.color}  # Include color information
                        for rental in qs]

        response.context_data['rentals_json'] = json.dumps(rentals_data)

        return response
