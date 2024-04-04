from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'rental'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
