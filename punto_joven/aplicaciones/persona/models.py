from django.db import models

class Persona(models.Model):
    nombre_completo=models.CharField('Nombre Completo', max_length=250, default=' ')
    
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.nombre_completo
    
