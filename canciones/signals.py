"""
Crea automáticamente un Perfil vacío cada vez que se crea un User nuevo,
ya sea por el formulario de registro o por `createsuperuser`. Así nunca
hay un usuario sin perfil, y el template puede asumir que
`user.perfil` siempre existe.
"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Perfil


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.get_or_create(user=instance)
