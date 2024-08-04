from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.ForeignKey('cursos.Curso', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
