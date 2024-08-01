# Este views contiene las vistas de la aplicacion cursos

from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/agregar_curso.html', {'form': form})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})

def buscar_curso(request):
    query = request.GET.get('q')
    resultados = Curso.objects.filter(nombre__icontains=query) if query else Curso.objects.all()
    return render(request, 'cursos/buscar_curso.html', {'resultados': resultados, 'query': query})
