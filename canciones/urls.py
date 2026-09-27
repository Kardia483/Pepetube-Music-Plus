from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_canciones, name="lista_canciones"),
    path("registro/", views.registro, name="registro"),
    path("borrar/<int:id>/", views.borrar_cancion, name="borrar_cancion"),
]
