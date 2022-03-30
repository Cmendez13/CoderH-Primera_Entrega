
from django.db import models

# Create your models here.
class Conductor(models.Model):
    primer_nombre=models.CharField(max_length=50,help_text='Introduzca el 1er Nombre')
    segundo_nombre=models.CharField(max_length=50,help_text='Introduzca el 2do Nombre')
    primer_apellido=models.CharField(max_length=50,help_text='Introduzca el 1er Apellido')
    segundo_apellido=models.CharField(max_length=50,help_text='Introduzca el 2do Apellido')
    dni=models.IntegerField(primary_key=True)
    fecha_de_nacimiento=models.DateField()
    vencimiento_dni=models.DateField()
    vencimiento_registro=models.DateField()
    sector=models.CharField(max_length=50)


    def __str__(self):

        return  self.primer_nombre + " " +self.primer_apellido +" (" +self.sector+")"


class Vehiculo(models.Model):
    marca=models.CharField(max_length=20,help_text='Introduzca la Marca')
    modelo=models.CharField(max_length=20,help_text='Introduzca el Modelo')
    dominio=models.CharField(max_length=20,help_text='Introduzca la Patente')

    def __str__(self):

        return self.marca+ " " + self.modelo +" " +self.dominio

class Asignacion(models.Model):
    
    fecha_asignacion=models.DateField()
    dominio=models.CharField(max_length=7)
    dni_conductor=models.IntegerField()

    def __str__(self):
        return str(self.fecha_asignacion) +" " + str(self.dominio)+ "" +str(self.dni_conductor)
    


