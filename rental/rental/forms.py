from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['auto', 'nombre', 'apellido', 'email', 'telefono', 'fecha_retiro', 'fecha_devolucion', 'observaciones', 'precio']