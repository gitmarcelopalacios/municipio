from django.db import models
from aplicaciones.empresa.models import Empresa
from aplicaciones.persona.models import Persona


class Emprendimiento(models.Model):
    nombre_emprendimiento=models.CharField('Nombre Emprendimiento', max_length=250, default=' ')
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.nombre_emprendimiento
    
    
