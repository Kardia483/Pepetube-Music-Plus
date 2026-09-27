from django.contrib.auth.models import User
from django.db import models


class Cancion(models.Model):
    """
    Modelo que representa una canción en la playlist de PepeTube Music Plus.

    Cumple con el requisito de "modelo con al menos 2 campos":
    - titulo  -> nombre de la canción
    - artista -> quién la canta / interpreta

    duracion, agregada e imagen son campos extra (no obligatorios en el
    formulario) que enriquecen el modelo y se pueden gestionar también
    desde el Django Admin.
    """

    titulo = models.CharField(max_length=120)
    artista = models.CharField(max_length=120)
    duracion = models.CharField(
        max_length=10,
        blank=True,
        help_text="Formato mm:ss, ej: 3:45 (opcional)",
    )
    imagen = models.ImageField(upload_to="portadas/", blank=True, null=True)
    agregada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-agregada"]
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"

    def __str__(self):
        return f"{self.titulo} — {self.artista}"


class Perfil(models.Model):
    """
    Datos extra del usuario que Django no trae por defecto (una foto de
    perfil). Se relaciona 1 a 1 con el modelo de usuario de Django, y se
    crea automáticamente para cada usuario nuevo (ver canciones/signals.py).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    foto = models.ImageField(upload_to="perfiles/", blank=True, null=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil de {self.user.username}"
