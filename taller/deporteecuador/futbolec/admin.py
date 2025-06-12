from django.contrib import admin
from .models import Equipo, Jugador, Campeonato, CampeonatoEquipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre_equipo', 'siglas', 'username')
    search_fields = ('nombre_equipo', 'siglas')


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_jugador', 'posicion', 'numero', 'sueldo', 'equipo')
    search_fields = ('nombre_jugador', 'posicion')


@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato', 'nombre_auspiciante')


@admin.register(CampeonatoEquipo)
class CampeonatoEquipoAdmin(admin.ModelAdmin):
    list_display = ('año', 'campeonato', 'equipo')
    search_fields = ('año', 'campeonato__nombre_campeonato', 'equipo__nombre_equipo')