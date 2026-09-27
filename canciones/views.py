from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegistroForm
from .models import Cancion, Perfil


def registro(request):
    """
    Vista de registro de usuarios nuevos: usa el formulario de Django
    (UserCreationForm) más una foto de perfil opcional. Al registrarse
    correctamente, deja al usuario con la sesión iniciada de una vez
    (no tiene que ir a /login/ aparte).
    """
    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # La señal en signals.py ya creó un Perfil vacío; lo actualizamos
            # con la foto que subió el usuario, si es que subió una.
            foto = form.cleaned_data.get("foto")
            if foto:
                perfil, _ = Perfil.objects.get_or_create(user=user)
                perfil.foto = foto
                perfil.save()
            login(request, user)
            return redirect("lista_canciones")
    else:
        form = RegistroForm()

    return render(request, "canciones/registro.html", {"form": form})


@login_required
def lista_canciones(request):
    """
    Vista que crea y lista canciones (el 'circuito completo' de la clase):

    1. El usuario escribe en las cajas de texto, elige una imagen y presiona el botón.
    2. El template envía los datos por POST a esta misma URL.
    3. La vista recibe los datos y usa el ORM para guardarlos.
    4. La vista consulta la lista actualizada y la manda al template.
    5. El template recorre la lista y la muestra en pantalla.

    Está protegida con @login_required: solo se puede ver la playlist
    si iniciaste sesión primero.
    """
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        artista = request.POST.get("artista")
        imagen = request.FILES.get("imagen")
        if titulo and artista:
            Cancion.objects.create(titulo=titulo, artista=artista, imagen=imagen)
        # Patrón POST-redirect-GET: evita que al recargar se reenvíe el form.
        return redirect("lista_canciones")

    canciones = Cancion.objects.all()
    return render(request, "canciones/lista.html", {"canciones": canciones})


@login_required
def borrar_cancion(request, id):
    """Elimina una canción de la playlist (operación Delete del CRUD)."""
    Cancion.objects.get(id=id).delete()
    return redirect("lista_canciones")
