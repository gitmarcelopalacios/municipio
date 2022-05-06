from django.contrib import admin
# Register your models here.
from .models import Proveedor
from aplicaciones.emprendimiento.models import Emprendimiento
from aplicaciones.tipodocumento.models import TipoDocumento
from aplicaciones.condicioniva.models import CondicionIVA

class ProveedorAdmin(admin.ModelAdmin):
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
        'emprendimiento',
        ) 
    search_fields = ('name',) 
    list_filter = ('emprendimiento',)  

admin.site.register(Proveedor, ProveedorAdmin)

