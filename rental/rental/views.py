from django.shortcuts import render

def index(request):

    variable = (3*2)

    return render(request, 'rental/index.html', {'variable': variable} )