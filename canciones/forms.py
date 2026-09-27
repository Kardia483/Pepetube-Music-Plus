from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    """
    Formulario de registro: el de Django (UserCreationForm) más un campo
    extra para subir una foto de perfil (opcional).
    """

    foto = forms.ImageField(required=False, label="Foto de perfil (opcional)")

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
