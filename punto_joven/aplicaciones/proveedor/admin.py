from django.contrib import admin
# Register your models here.
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'domicilio',
        )    

admin.site.register(Proveedor)