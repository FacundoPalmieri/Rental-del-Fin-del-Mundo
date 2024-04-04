from django.shortcuts import render
from django.http import JsonResponse
from .models import Auto, Rental, Plan
from datetime import datetime, timedelta
from .forms import RentalForm
def index(request):

    #http://localhost:8000?start_date=2024-04-03&end_date=2024-04-10
    available_autos_data = None
    difference = None
    difference_days = None

    if request.method == 'GET':
        # Get parameters from the request
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        # Check if parameters are provided
        if start_date_str is None or end_date_str is None:
            return render(request, 'rental/index.html', {'autos_disponbiles': available_autos_data} )

        # Convert string dates to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        # Query rentals that overlap with the given period
        overlapping_rentals = Rental.objects.filter(
            fecha_retiro__lte=end_date,
            fecha_devolucion__gte=start_date
        )

        # Get the list of autos from overlapping rentals
        unavailable_autos = [rental.auto.id for rental in overlapping_rentals]

        # Get all autos
        all_autos = Auto.objects.all()

        # Filter available autos
        available_autos = all_autos.exclude(id__in=unavailable_autos)


        difference = end_date - start_date
        difference_days = difference.days
        dias = None

        if difference == timedelta(days=1):
            dias = 'un_dia'
        elif timedelta(days=2) <= difference <= timedelta(days=3):
            dias = 'dos_a_tres'
        elif timedelta(days=4) <= difference <= timedelta(days=6):
            dias = 'cuatro_a_seis'
        elif difference.days >= 7:
            dias = 'siete_o_mas'

        # Serialize available autos data
        available_autos_data = [
            {
                'id': auto.id,
                'marca': auto.marca,
                'modelo': auto.modelo,
                'anio': auto.anio,
                'imagen': auto.imagen,
                'puertas': auto.puertas,
                'pasajeros': auto.pasajeros,
                'color': auto.color,
                'tipo': auto.tipo,
                'baul': auto.baul,
                'caja': auto.caja,
                'plan': auto.plan,
                'precio_total': (getattr(Plan.objects.get(tipo=auto.plan, trimestre='Marzo/Abril/Mayo'), dias) * difference.days),
                'precio_por_dia': getattr(Plan.objects.get(tipo=auto.plan, trimestre='Marzo/Abril/Mayo'), dias),
                # Add other fields you want to include
            }
            for auto in available_autos
        ]

    gracias = False

    if request.method == 'POST':
        form = RentalForm(request.POST)
        print(11)
        if form.is_valid():
            print(22)
            form.save()
            print(33)
            gracias = True
            print('gracias', gracias)
            return render(request, 'rental/index.html', {'autos_disponbiles': available_autos_data, 'dias': difference_days, 'form': form, 'gracias': gracias} )
            # Redirect or do something upon successful form submission
        else:
            print(form.errors)
    else:
        form = RentalForm()

    return render(request, 'rental/index.html', {'autos_disponbiles': available_autos_data, 'dias': difference_days, 'form': form, 'gracias': gracias} )