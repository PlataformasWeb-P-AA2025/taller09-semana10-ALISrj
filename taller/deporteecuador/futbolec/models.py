from django.db import models


# Create your models here.

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100, unique=True)
    siglas = models.CharField(max_length=100, blank=True)  # el campo puede
    username = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_equipo} ({self.siglas})'


class Jugador(models.Model):
    nombre_jugador = models.CharField(max_length=100, unique=True)
    posicion = models.CharField(max_length=100, blank=True)  # el campo puede
    numero = models.IntegerField()
    sueldo = models.DecimalField(decimal_places=2, max_digits=10)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_jugador} - #{self.numero} ({self.posicion})'


class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100, unique=True)
    nombre_auspiciante = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre_campeonato


class CampeonatoEquipo(models.Model):
    año = models.CharField(max_length=30, blank=True)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.campeonato} - {self.equipo} ({self.año})'
