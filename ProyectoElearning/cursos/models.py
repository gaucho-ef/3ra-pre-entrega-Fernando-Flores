from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    profesor = models.ForeignKey('profesores.Profesor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
