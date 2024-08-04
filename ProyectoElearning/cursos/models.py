# cursos/models.py

from django.db import models
from profesores.models import Profesor  # Importar explícitamente el modelo Profesor

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = '2023.01.11'#models.DateField()
    fecha_fin = '2026.12.22' #models.DateField()
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)  # Usar el modelo Profesor importado

    def __str__(self):
        return self.nombre
