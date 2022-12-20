from django.contrib import admin
from .models import Becas
# Register your models here.

#admin.site.register(Becas)

@admin.register(Becas)
class BecasModel(admin.ModelAdmin):
    list_filter = ('nombre', 'porcentaje')
    list_display = ('nombre', 'porcentaje', 'universidad')