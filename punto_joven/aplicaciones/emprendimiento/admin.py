from django.contrib import admin
# Register your models here.
from .models import Emprendimiento

class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'persona',
        )    
    search_fields = ('name',)

admin.site.register(Emprendimiento, EmprendimientoAdmin)
