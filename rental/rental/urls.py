
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='index.html'),
]




