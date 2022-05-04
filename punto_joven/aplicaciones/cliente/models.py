from django.db import models
from aplicaciones.emprendimiento.models import Emprendimiento

class Cliente(models.Model):
    cliente=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    nombre_cliente=models.CharField('Nombre Completo', max_length=250, default=' ')
    
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.nombre_cliente
    
