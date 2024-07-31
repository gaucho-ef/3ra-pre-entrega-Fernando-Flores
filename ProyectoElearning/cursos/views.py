# Este views contiene las vistas de la aplicacion cursos

from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm, ProfesorForm, AlumnoForm

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/index.html', {'cursos': cursos})

def buscar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        resultados = Curso.objects.filter(nombre__icontains=query)
        return render(request, 'cursos/buscar.html', {'resultados': resultados})
    return render(request, 'cursos/buscar.html')

def agregar(request):
    if request.method == 'POST':
        curso_form = CursoForm(request.POST)
        profesor_form = ProfesorForm(request.POST)
        alumno_form = AlumnoForm(request.POST)
        if curso_form.is_valid() and profesor_form.is_valid() and alumno_form.is_valid():
            curso_form.save()
            profesor_form.save()
            alumno_form.save()
            return redirect('index')
    else:
        curso_form = CursoForm()
        profesor_form = ProfesorForm()
        alumno_form = AlumnoForm()
    return render(request, 'cursos/agregar.html', {'curso_form': curso_form, 'profesor_form': profesor_form, 'alumno_form': alumno_form})
