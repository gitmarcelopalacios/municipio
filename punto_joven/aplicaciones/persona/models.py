from django.db import models
from aplicaciones.tipodocumento.models import TipoDocumento
from aplicaciones.condicioniva.models import CondicionIVA
class Persona(models.Model):
    name=models.CharField('Alumno', max_length=250, default=' ')
    dom=models.CharField('Domicilio', max_length=250, default=' ')
    tipodocumento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,default=1)
    numdoc=models.CharField('Número de documento', max_length=15, default=' ')
    condicioniva=models.ForeignKey(CondicionIVA, on_delete=models.CASCADE,default=1)
    numconiva=models.CharField('Número de CUIT', max_length=20, default=' ')
    avatar = models.ImageField(upload_to='fotoalumno', blank=True, null=True)
    class Meta:
        verbose_name = 'Alumno Emprendedor'
        verbose_name_plural = 'Alumnos Emprendedores'
        
    
    
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name
    
