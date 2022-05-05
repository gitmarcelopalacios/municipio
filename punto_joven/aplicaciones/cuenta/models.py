from django.db import models

class Cuenta(models.Model):
    name=models.CharField('Cuenta', max_length=250, default=' ')

    class Meta:
        verbose_name = 'Cuenta Contable'
        verbose_name_plural = 'Cuentas Contables'   
        ordering = ['name']

    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name