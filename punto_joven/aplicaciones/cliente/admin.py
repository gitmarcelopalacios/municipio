from django.contrib import admin
# Register your models here.
from .models import Cliente
from aplicaciones.emprendimiento.models import Emprendimiento
from aplicaciones.tipodocumento.models import TipoDocumento
from aplicaciones.condicioniva.models import CondicionIVA

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'tipodocumento',
        'numdoc',
        'condicioniva',
        'numconiva',
        'dom',
        'tel',
        'emprendimiento'
        )    

admin.site.register(Cliente, ClienteAdmin)

