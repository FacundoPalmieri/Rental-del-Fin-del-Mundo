from django import forms
from .models import Rental
from colorfield.widgets import ColorWidget
class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['auto', 'nombre', 'apellido', 'email', 'telefono', 'fecha_retiro', 'fecha_devolucion', 'observaciones', 'precio', 'color']
        widgets = {
                'color': ColorWidget(attrs={'style': 'width: 100px; height: 30px;'})
        }
        
    def clean_color(self):
        color = self.cleaned_data['color']
        if not color.startswith('#'):
            color = '#' + color
        return color