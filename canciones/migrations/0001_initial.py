import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cancion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=120)),
                ("artista", models.CharField(max_length=120)),
                (
                    "duracion",
                    models.CharField(
                        blank=True,
                        help_text="Formato mm:ss, ej: 3:45 (opcional)",
                        max_length=10,
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="portadas/"),
                ),
                ("agregada", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Canción",
                "verbose_name_plural": "Canciones",
                "ordering": ["-agregada"],
            },
        ),
        migrations.CreateModel(
            name="Perfil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "foto",
                    models.ImageField(blank=True, null=True, upload_to="perfiles/"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="perfil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil",
                "verbose_name_plural": "Perfiles",
            },
        ),
    ]
