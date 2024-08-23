from django.db import models

# Create your models here.

class Tareas(models.Model):
    estados = [{'terminado':'Tarea finalizada'},
               {'incompleto':'Tarea incompleta'}]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estado = models.CharField(choices=estados,default='incompleto')
    def __str__(self):
        return self.titulo

