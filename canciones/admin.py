from django.contrib import admin

from .models import Cancion, Perfil


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "artista", "duracion", "agregada")
    list_filter = ("artista",)
    search_fields = ("titulo", "artista")


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("user", "foto")
