from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "index.html",
        titulo="Inicio",
        mensaje="Te damos la bienvenida a la Biblioteca Universitaria.",
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        titulo="Catálogo",
        mensaje="Explora los materiales disponibles para apoyar tu aprendizaje e investigación.",
    )


@app.route("/servicios")
def servicios():
    return render_template(
        "servicios.html",
        titulo="Servicios",
        mensaje="Conoce los servicios que ponemos a tu disposición.",
    )


@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        titulo="Contacto",
        mensaje="Estamos aquí para ayudarte. Estos son nuestros medios de contacto.",
    )


if __name__ == "__main__":
    app.run(debug=True)