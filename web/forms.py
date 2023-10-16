from django.forms import ModelForm
from .models import *

class ProfesorForm(ModelForm):
    class Meta:
        model = TblProfesor
        fields = '__all__'
        
class AlumnoForm(ModelForm):
    class Meta:
        model = TblAlumno
        fields = '__all__'

