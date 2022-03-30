from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='blog_home'),
    path('listarConductores/', views.listarConductores, name='listar_conductores'),
    path('listarVehiculos/', views.listarVehiculos, name='listar_vehiculos'),
    path('listarAsignaciones/', views.listarAsignaciones, name='listar_asignaciones'),
    path('ingresarConductor/',views.conductor,name='ingresar_conductor'),
    path('ingresarVehiculo/',views.vehiculo,name='ingresar_vehiculo'),
    path('ingresarAsignacion/',views.asignacion,name='ingresar_asignacion'),
    path('busqueda/',views.busqueda,name='realizar_busqueda'),
]