# ------- 31/07/2024 ---- fernando flores ---------
# ------- links de alumnos ------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alumnos, name='listar_alumnos'),
    path('agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('editar/<int:pk>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar/<int:pk>/', views.eliminar_alumno, name='eliminar_alumno'),
]
