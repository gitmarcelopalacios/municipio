from django.db import models
from aplicaciones.emprendimiento.models import Emprendimiento
from aplicaciones.tipodocumento.models import TipoDocumento
from aplicaciones.condicioniva.models import CondicionIVA

class Cliente(models.Model):
    name=models.CharField('Cliente', max_length=250, default=' ')
    dom=models.CharField('Domicilio', max_length=250, default='Completar')
    tel=models.CharField('Teléfono', max_length=250, default=' ')
    email = models.EmailField('Email', max_length=254,default='desconocido@email.com')
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    tipodocumento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,default=1)
    numdoc=models.CharField('Número de documento', max_length=15, default='Completar')
    condicioniva=models.ForeignKey(CondicionIVA, on_delete=models.CASCADE,default=1)
    numconiva=models.CharField('Número de CUIT', max_length=20, default='Completar')
    avatar = models.ImageField(upload_to='fotoalumno', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cliente del Emprendimiento'
        verbose_name_plural = 'Clientes de Emprendimientos'
    
   
    def __str__(self):
        #return str(self.id)+' - '+self.nombre_completo
        return self.name
    

    
