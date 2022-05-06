from django.contrib import admin
# Register your models here.
from .models import Cuenta

class CuentaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        )    

admin.site.register(Cuenta,CuentaAdmin)
