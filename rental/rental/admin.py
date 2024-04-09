from django.contrib import admin
from .models import *
from django.urls import reverse
import json
from .forms import *

admin.site.register(Plan)
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
