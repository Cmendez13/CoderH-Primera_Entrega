from django import forms


class ConductorFormulario(forms.Form):   
    primer_nombre= forms.CharField(max_length=50)
    segundo_nombre= forms.CharField(max_length=50,required=False)
    primer_apellido= forms.CharField(max_length=50)
    segundo_apellido= forms.CharField(max_length=50,required=False)
    dni= forms.IntegerField()
    fecha_de_nacimiento=forms.DateField()
    vencimiento_dni= forms.DateField()
    vencimiento_registro=forms.DateField()
    sector=forms.CharField(max_length=50)

class VehiculoFormulario(forms.Form):
    modelo= forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)  
    dominio = forms.CharField(max_length=7)

class AsignacionFormulario(forms.Form):
    
    fecha_asignacion= forms.DateField()
    dominio = forms.CharField(max_length=7)  
    dni_conductor = forms.IntegerField()


    
    


