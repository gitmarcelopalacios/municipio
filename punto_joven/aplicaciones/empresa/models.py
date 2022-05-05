from django.db import models

class Empresa(models.Model):
    name=models.CharField('Razón Social', max_length=250, default=' ')

    class Meta:
        verbose_name = 'Empresa del Alumno'
        verbose_name_plural = 'Empresas de los Alumnos'   
        ordering = ['name']
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name
