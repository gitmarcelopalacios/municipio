from django.db import models

class TipoDocumento(models.Model):
    name=models.CharField('Tipo de documento', max_length=250, default=' ')

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'   
        ordering = ['name']
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name