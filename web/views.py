from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TblAlumno
from .models import TblProfesor
from .forms import AlumnoForm
from .forms import ProfesorForm


# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request, alumno_id=None):
        if alumno_id:
            alumno = get_object_or_404(TblAlumno, alumno_id=alumno_id)
            alumno.delete()
            return redirect('/')
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')

class ProfesorView(View):
    
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'profesores.html',context)  

    def post(self, request, profesor_id=None):
        if profesor_id:  
           profesor = get_object_or_404(TblProfesor, profesor_id=profesor_id)
           profesor.delete()
           return redirect('web:profesores')
        else: 
           formProfesor = ProfesorForm(request.POST)
           if formProfesor.is_valid():
               formProfesor.save()
               return redirect('web:profesores')
           else:
               context = {
                   'profesores': TblProfesor.objects.all(),
                   'formProfesor': formProfesor
               }
               return render(request, 'profesores.html', context)