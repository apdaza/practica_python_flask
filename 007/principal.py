from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        lista = [x.split(',') for x in open(f.filename).readlines()]
        resultados = []
        for x in lista:
            r = sum([int(y) for y in x])
            resultados.append(x + [r])
        return render_template('resultados.html', datos=resultados)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)