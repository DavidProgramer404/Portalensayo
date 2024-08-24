from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Nota(models.Model):
    tipos = (("urgente", "Urgente"), ("normal", "Normal"))

    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    tipo = models.CharField(max_length=20, choices=tipos)


class UserProfile(models.Model):
    roles = (("Cliente", "Cliente"), ("Operario", "Operario"))

    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE
    )
    rol = models.CharField(max_length=100, choices=roles)

    def __str__(self):
        return f'{self.user.username} ({self.rol})'


# categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


# Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.URLField(max_length=255)
    estados = (
        ("disponible", "disponible"),
        ("arrendado", "arrendado"),
        ("mantención", "mantención"),
    )
    estado = models.CharField(max_length=20, choices=estados)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# Class Arriendo

class Arriendo(models.Model):
    fecha = models.DateField()
    observacion = models.TextField()
    dañado = models.BooleanField(default=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha

