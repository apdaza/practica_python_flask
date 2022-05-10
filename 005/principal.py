from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<nombre>')
def saludador_nombre(nombre):
    datos = {'001': 'alejo', '002': 'juan', '003': 'pedro'}
    return render_template('index.html', nombre=nombre, usuarios=datos)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
