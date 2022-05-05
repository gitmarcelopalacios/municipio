from pickle import FALSE
from django.db import models
from aplicaciones.cuenta.models import Cuenta

class DetalleCuenta(models.Model):
    name=models.CharField('Nota Explicativa', max_length=250, default=' ')
    cuenta=models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    asiento = models.IntegerField()
    fecha = models.DateField()
    importe = models.DecimalField('Débito(+)/Crédito(-)', max_digits=18, decimal_places=2)

    class Meta:
        verbose_name = 'Partida Contable'
        verbose_name_plural = 'Partidas Contables'   
        ordering = ['name']
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name
    
    
    
    