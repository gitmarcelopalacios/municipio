from django.contrib import admin
# Register your models here.
from .models import CondicionIVA


class CondicionIVAAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        )    

admin.site.register(CondicionIVA, CondicionIVAAdmin)
