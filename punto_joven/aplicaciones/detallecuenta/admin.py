from django.contrib import admin
# Register your models here.
from .models import DetalleCuenta
from .models import Cuenta



class DetalleCuentaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'asiento'
        'fecha',
        'cuenta',
        'name',        
        'importe', 
    )

admin.site.register(DetalleCuenta, DetalleCuentaAdmin)
