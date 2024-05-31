
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

    tipo = models.CharField(choices=TIPO, max_length=50)
    enero  = models.DecimalField(max_digits=50, decimal_places=3)
    febrero = models.DecimalField(max_digits=50, decimal_places=3)
    marzo = models.DecimalField(max_digits=50, decimal_places=3)
    abril = models.DecimalField(max_digits=50, decimal_places=3)
    mayo = models.DecimalField(max_digits=50, decimal_places=3)
    junio = models.DecimalField(max_digits=50, decimal_places=3)
    julio = models.DecimalField(max_digits=50, decimal_places=3)
    agosto = models.DecimalField(max_digits=50, decimal_places=3)
    septiembre = models.DecimalField(max_digits=50, decimal_places=3)
    octubre = models.DecimalField(max_digits=50, decimal_places=3)
    noviembre = models.DecimalField(max_digits=50, decimal_places=3)
    diciembre = models.DecimalField(max_digits=50, decimal_places=3)

    hora_extra = models.DecimalField(max_digits=50, decimal_places=3)

    def __str__(self):
        return f"{self.tipo}"

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

    COLOR_PALETTE = [
        ("#549ccc", "azul", ),
        ("#59af80", "verde", ),
        ("#de583d", "naranja", ),
        ("#aa61bb", "violeta", ),             
    ]
        
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_retiro = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    devuelto = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=50, decimal_places=3)
    color = ColorField(default='#89CFF0', blank=True, null=True, samples=COLOR_PALETTE)

    def __str__(self):
        return f"{self.auto} / {self.nombre} {self.apellido}"