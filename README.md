# Biblioteca Universitaria

Sitio web informativo desarrollado con **Flask**, **Jinja2** y **Bootstrap**. Presenta información general de una biblioteca universitaria ficticia y permite navegar entre sus páginas principales.

## Elementos implementados

### Aplicación Flask

El archivo `server.py` es el punto de entrada de la aplicación. Crea la instancia de Flask y define cuatro rutas. Cada ruta utiliza `render_template()` para cargar la plantilla correspondiente y enviar las variables `titulo` y `mensaje`.

| Ruta | Página | Plantilla |
|---|---|---|
| `/` | Inicio | `templates/index.html` |
| `/catalogo` | Catálogo | `templates/catalogo.html` |
| `/servicios` | Servicios | `templates/servicios.html` |
| `/contacto` | Contacto | `templates/contacto.html` |

### Plantilla base y navegación

`templates/layout.html` contiene la estructura HTML compartida por todas las páginas:

- Define el idioma del documento como español y configura la vista para distintos tamaños de pantalla.
- Carga **Bootstrap 5.3.3** desde una CDN.
- Muestra el nombre **Biblioteca Universitaria** como identificador del sitio.
- Incluye una barra de navegación horizontal con enlaces a Inicio, Catálogo, Servicios y Contacto. Los enlaces se generan con `url_for()` para apuntar a las rutas de Flask.
- Usa un estilo visual neutro con fondo claro y borde inferior.
- Define el área `container-fluid` y el bloque Jinja `{% block content %}` donde se inserta el contenido de cada página.

### Páginas

Las cuatro plantillas hijas extienden `layout.html` mediante `{% extends "layout.html" %}` y colocan su contenido dentro de `{% block content %}`:

- **Inicio (`index.html`):** presenta el nombre de la biblioteca, un mensaje de bienvenida, su propósito y el horario general.
- **Catálogo (`catalogo.html`):** introduce los materiales disponibles y describe las categorías de libros, revistas, tesis y recursos digitales.
- **Servicios (`servicios.html`):** describe el préstamo de libros, la consulta en sala, el acceso a recursos digitales y la orientación bibliográfica.
- **Contacto (`contacto.html`):** muestra la dirección, el correo electrónico y el horario de atención.

La dirección y los datos de contacto son ficticios, para fines del ejercicio.

## Cómo ejecutar

1. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

2. Inicia el servidor desde la carpeta del proyecto:

   ```bash
   python server.py
   ```

3. Abre `http://127.0.0.1:5000/` en el navegador. Utiliza el menú para visitar las demás páginas.