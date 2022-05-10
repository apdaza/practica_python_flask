from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return "Hola Mundo"

@app.route('/<nombre>')
def saludador_nombre(nombre):
    return "Hola " + nombre

@app.route('/<int:pos>')
def posicion(pos):
    return "hola: " * pos

@app.route('/<float:costo>')
def costo(costo):
    return "Costo: %f" % costo

if __name__ == '__main__':
    app.run(debug=True, port=8080)