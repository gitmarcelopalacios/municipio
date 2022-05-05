from django.db import models

class CondicionIVA(models.Model):
    name=models.CharField('Condicion', max_length=250, default=' ')

    class Meta:
        verbose_name = 'Condición de I.V.A.'
        verbose_name_plural = 'Condiciones de I.V.A.'   
        ordering = ['name']
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name