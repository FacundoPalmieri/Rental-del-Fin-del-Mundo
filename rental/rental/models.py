
from django.db import models
from colorfield.fields import ColorField
from django.db import models
from decimal import Decimal
class Plan(models.Model):
    class Meta:
        verbose_name_plural = 'planes'

    TIPO = (
        ('Basico','Basico'),
        ('Estandar','Estandar'),
        ('Pro','Pro')
    )

    TRIMESTRE = (
        ('Marzo/Abril/Mayo','Marzo/Abril/Mayo'),
        ('Junio/Julio/Agosto','Junio/Julio/Agosto'),
        ('Septiembre/Octubre/Noviembre','Septiembre/Octubre/Noviembre'),
        ('Diciembre/Enero/Febrero','Diciembre/Enero/Febrero')
    )

    tipo = models.CharField(choices=TIPO, max_length=50)
    un_dia = models.DecimalField(max_digits=50, decimal_places=3)
    hora_extra = models.DecimalField(max_digits=50, decimal_places=3)
    trimestre = models.CharField(choices=TRIMESTRE, max_length=50)

    # Add discount percentages for each type
    discount_percentages = {
        'Basico': {'dos_a_tres': Decimal('7.69'), 'cuatro_a_seis': Decimal('10.26'), 'siete_o_mas': Decimal('12.82')},
        'Estandar': {'dos_a_tres': Decimal('6.98'), 'cuatro_a_seis': Decimal('9.30'), 'siete_o_mas': Decimal('11.63')},
        'Pro': {'dos_a_tres': Decimal('4.55'), 'cuatro_a_seis': Decimal('6.06'), 'siete_o_mas': Decimal('7.58')}
    }

    def dos_a_tres(self):
        return round(self.un_dia * (1 - self.discount_percentages[self.tipo]['dos_a_tres'] / Decimal('100')), 3)

    def cuatro_a_seis(self):
        return round(self.un_dia * (1 - self.discount_percentages[self.tipo]['cuatro_a_seis'] / Decimal('100')), 3)

    def siete_o_mas(self):
        return round(self.un_dia * (1 - self.discount_percentages[self.tipo]['siete_o_mas'] / Decimal('100')), 3)

    def __str__(self):
        return f"{self.tipo} {self.trimestre}"

class Auto(models.Model):
    CAJA = (
        ('Automatica','Automatica'),
        ('Manual','Manual')
    )
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()    
    imagen = models.ImageField(upload_to='static/images')
    puertas = models.PositiveSmallIntegerField()
    tipo = models.CharField(max_length=50)
    pasajeros = models.PositiveSmallIntegerField()
    baul = models.BooleanField(default=False)
    color = models.CharField(max_length=50)
    caja = models.CharField(choices=CAJA)
    plan = models.CharField(choices=Plan.TIPO)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.color}"

class Rental(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_retiro = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=50, decimal_places=3)
    color = ColorField(default='#89CFF0', blank=True, null=True)

    def __str__(self):
        return f"{self.auto} / {self.nombre} {self.apellido}"