from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Estudiante, Modulo, Matricula
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class Equipo(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante')
    search_fields = ('nombre', 'cedula')
    exclude = ("modulos",) # se excluye de la interfaz del admin

admin.site.register(Estudiante, EstudianteAdmin)

class Jugador(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('estudiante', 'modulo', 'comentario')
    search_fields = ('estudiante__nombre', 'modulo__nombre')

admin.site.register(Matricula, MatriculaAdmin)

class Campeonato(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('estudiante', 'modulo', 'comentario')
    search_fields = ('estudiante__nombre', 'modulo__nombre')

admin.site.register(Matricula, MatriculaAdmin)

class CampeonatoEquipo(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('estudiante', 'modulo', 'comentario')
    search_fields = ('estudiante__nombre', 'modulo__nombre')

admin.site.register(Matricula, MatriculaAdmin)
