from django.db import models

class CondicionIVA(models.Model):
    name=models.CharField('Condicion', max_length=250, default=' ')

    class Meta:
        ordering = ['name']
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name