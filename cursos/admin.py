from django.contrib import admin
from .models import Cursos

class CursosDisplay(admin.ModelAdmin):
    list_display = ('id','nome_curso_bosch', 'nome_curso_senai', 'qtd_aprendizes', 'descritivo' )
# Register your models here.

admin.site.register(Cursos, CursosDisplay)
