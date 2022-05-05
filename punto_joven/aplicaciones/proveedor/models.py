from django.db import models
from aplicaciones.emprendimiento.models import Emprendimiento

class Proveedor(models.Model):
    name=models.CharField('Proveedor', max_length=250, default=' ')
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    domicilio=models.CharField('Domicilio', max_length=250, default=' ')
    
    # class Meta:
    #     verbose_name = 'Customercito'
    #     verbose_name_plural = 'CUSTOMERCITOS'
    
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name
    
