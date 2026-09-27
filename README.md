# PepeTube Music Plus 🐱🎧

Versión "Plus" del proyecto **PepeTube Music**, para la tarea de Semana 5
(Django ORM, Admin y CRUD) de Programación Back End — INACAP.

Sobre la misma base del proyecto anterior (playlist con alta, listado y
eliminación de canciones), esta versión agrega:

- Un template base (`base.html`) que comparten todas las páginas.
- Inicio de sesión (login) y cierre de sesión (logout) con el sistema de
  autenticación de Django.
- Registro de usuarios nuevos (`/registro/`).
- Foto de perfil por usuario (`foto = user`, modelo `Perfil` 1 a 1 con `User`).
- Playlist protegida: solo se puede ver y editar si iniciaste sesión.
- Nueva paleta de colores: negro, morado y blanco.

## Requisitos que cumple (rúbrica)

- **5.1 — Modelo con Django ORM:** `canciones/models.py` define `Cancion`
  (título, artista, duración, imagen, fecha) y `Perfil` (usuario, foto),
  ambos gestionados con el ORM (`.objects.create()`, `.all()`, `.get()`,
  `.delete()`).
- **5.2 — Formulario + Admin:** un formulario con dos campos de texto
  (título y artista) más un botón "Agregar", que guarda directamente en la
  base de datos y llena la lista visible en pantalla. Ambos modelos están
  registrados en `canciones/admin.py` y son editables desde `/admin/`.
- **5.3 — Listado + eliminar:** la playlist se muestra completa en
  `lista.html`, y cada canción tiene su propio botón para eliminarla
  (`borrar_cancion`).

Además: login (`/login/`), logout (POST, botón "Cerrar sesión") y registro
(`/registro/`) con foto de perfil opcional.

## Estructura del proyecto

```
pepetube_music_plus/
├── manage.py
├── requirements.txt
├── pepetube_music_plus/       # configuración del proyecto (settings, urls)
└── canciones/                 # la app con el modelo, vistas y templates
    ├── models.py               # Cancion, Perfil
    ├── forms.py                 # RegistroForm (UserCreationForm + foto)
    ├── signals.py                # crea un Perfil vacío para cada user nuevo
    ├── views.py                  # registro, lista_canciones, borrar_cancion
    ├── admin.py
    ├── urls.py
    ├── static/canciones/logo.jpg
    └── templates/
        ├── base.html              # header, nav, estilos, compartido
        └── canciones/
            ├── lista.html         # playlist (extiende base.html)
            ├── login.html         # inicio de sesión
            └── registro.html      # crear cuenta
```

## Cómo correrlo (Windows / PowerShell)

1. Ve a la carpeta del proyecto:
   ```
   cd "Escritorio\Programacion\Back End\Pepetube Music Plus"
   ```

2. Crea y activa un entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Aplica las migraciones (crea la base de datos):
   ```
   python manage.py migrate
   ```

5. Crea un usuario administrador (para entrar a `/admin/`):
   ```
   python manage.py createsuperuser
   ```

6. Corre el servidor:
   ```
   python manage.py runserver
   ```

7. Abre el navegador en:
   - `http://127.0.0.1:8000/` → te pedirá iniciar sesión primero
   - `http://127.0.0.1:8000/login/` → iniciar sesión
   - `http://127.0.0.1:8000/registro/` → crear una cuenta nueva (con foto
     de perfil opcional)
   - `http://127.0.0.1:8000/admin/` → panel de administración (con el
     usuario del paso 5)

## Notas

- Las fotos de portada y de perfil se guardan en la carpeta `media/`
  (se crea sola la primera vez que subes una imagen).
- Si Pillow no está instalado, subir imágenes va a fallar: revisa que el
  `pip install -r requirements.txt` se haya ejecutado dentro del `venv`.
- El logo (gato con pañuelo rojo) está en
  `canciones/static/canciones/logo.jpg`.
