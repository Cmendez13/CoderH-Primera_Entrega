from email import message
from django import views
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    context={

        'Conductores':Conductor.objects.all()
    }
    return render(request,'inicio.html')


def listarConductores(request):
    conductores=Conductor.objects.all()

    return render(request,'listar_conductores.html',{'conductores':conductores})

def listarVehiculos(request):
    vehiculos=Vehiculo.objects.all()

    return render(request,'listar_vehiculos.html',{'vehiculos':vehiculos})

def listarAsignaciones(request):
    asignaciones=Asignacion.objects.all()
    
    
    
    return render(request,'listar_asignaciones.html',{'asignaciones':asignaciones})


def conductor(request):

      if request.method == 'POST':

            conductor_formulario = ConductorFormulario(request.POST) #aquí mellega toda la información del html

            print(conductor_formulario)

            if conductor_formulario.is_valid:   #Si pasó la validación de Django

                  data = conductor_formulario.cleaned_data

                  conductor = Conductor(primer_nombre=data['primer_nombre'].title(),segundo_nombre=data['segundo_nombre'].title()
                  , primer_apellido=data['primer_apellido'].title(), segundo_apellido=data['segundo_apellido'].title(),
                  dni=data['dni'],fecha_de_nacimiento=data['fecha_de_nacimiento'],
                  vencimiento_dni=data['vencimiento_dni'],vencimiento_registro=data['vencimiento_registro'],
                  sector=data['sector'].title()) 

                  conductor.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            conductor= ConductorFormulario() #Formulario vacio para construir el html

      return render(request, "formulario_conductor.html", {"ConductorFormulario":conductor})


def vehiculo(request):

      if request.method == 'POST':

            vehiculo_formulario = VehiculoFormulario(request.POST) #aquí mellega toda la información del html

            print(vehiculo_formulario)

            if vehiculo_formulario.is_valid:   #Si pasó la validación de Django

                  data = vehiculo_formulario.cleaned_data

                  vehiculo = Vehiculo(marca=data['marca'].title(),
                  modelo=data['modelo'].title(),dominio=data['dominio'].upper()) 

                  vehiculo.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            vehiculo= VehiculoFormulario() #Formulario vacio para construir el html

      return render(request, "formulario_vehiculo.html", {"VehiculoFormulario":vehiculo})



def asignacion(request):

      if request.method == 'POST':

            asignacion_formulario = AsignacionFormulario(request.POST) #aquí mellega toda la información del html

            print(asignacion_formulario)

            if asignacion_formulario.is_valid:   #Si pasó la validación de Django

                  data = asignacion_formulario.cleaned_data
                  
                  asignacion = Asignacion(fecha_asignacion=data['fecha_asignacion'],
                  dominio=data['dominio'].upper(),dni_conductor=data['dni_conductor']) 

                  asignacion.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            asignacion= AsignacionFormulario() #Formulario vacio para construir el html

      return render(request, "formulario_asignacion.html", {"AsignacionFormulario":asignacion})

def busqueda(request):
      #consulta=None
      
      consulta=request.GET.get("q")
      print(consulta)

      if consulta==None:

             
            return render(request,"busqueda.html",{'consulta':None,'resultados':None})

      else:

            resultados= Conductor.objects.filter(dni__icontains=consulta)
            print(resultados)
            return render(request, "busqueda.html", {'consulta':consulta,'resultados':resultados})

      

      #return render(request,"inicio.html",{"message":message})

            