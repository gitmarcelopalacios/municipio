from django.db import models
from aplicaciones.empresa.models import Empresa
from aplicaciones.persona.models import Persona
from ckeditor.fields import RichTextField


class Emprendimiento(models.Model):
    name=models.CharField('Nombre Emprendimiento', max_length=250, default=' ')
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    anotaciones=RichTextField()
    class Meta:
        verbose_name = 'Emprendimiento del Alumno'
        verbose_name_plural = 'Emprendimiento de Alumnos'   
        ordering = ['name']

    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name
    
    
