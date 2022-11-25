from flask import Flask,request, render_template
import os

app = Flask(__name__)

def buscaPalabras(buscar):
    dicHadoop = hadoopFiletoDict()
    resultado = {}
    
    for element in buscar:
        if buscar.count(element) > 1:
            buscar.remove(element)

    for x in buscar:
        if x in dicHadoop:
            while len(dicHadoop[x]) != 0:
                resultado['/resultados?resultado=%s&archivo=%s' % (x, dicHadoop[x][0])] = int(dicHadoop[x][1])
                dicHadoop[x].pop(0)
                dicHadoop[x].pop(0)
        else:
            resultado['No hay coincidencia para \"%s\".' % (x)] = 0

    listaHadoop = list(resultado.items())
    
    return listaHadoop

def hadoopFiletoDict():
    archivo = open('../jobs/data/final/final.txt')
    lineas = archivo.readlines()

    dicHadoop = {}

    for linea in lineas:
        linea = linea.split('¬')
        dicHadoop[linea.pop(0)] = linea
    
    return dicHadoop

@app.route('/', methods = ['GET'])
def index():

    return render_template("index.html")

@app.route('/busqueda', methods = ['GET'])
def busqueda():

    buscar = request.args.get('busqueda')

    listaHadoop = buscaPalabras(buscar.split(' '))

    for mx in range(len(listaHadoop)-1, -1, -1):
        swapped = False
        for i in range(mx):
            if int(listaHadoop[i][1]) < int(listaHadoop[i+1][1]):
                listaHadoop[i], listaHadoop[i+1] = listaHadoop[i+1], listaHadoop[i]
                swapped = True
        if not swapped:
            break

    return render_template("url.html", urls = listaHadoop)

@app.route('/resultados', methods = ['GET'])
def resultados():

    if os.path.isfile('../jobs/data/carpeta1/%s' % (request.args.get('archivo'))):
        return render_template('archivo.html', archivo = open('../jobs/data/carpeta1/%s' % (request.args.get('archivo'))).read().split(request.args.get('archivo'))[1])
    else:
        return render_template('archivo.html', archivo = open('../jobs/data/carpeta2/%s' % (request.args.get('archivo'))).read().split(request.args.get('archivo'))[1])

if __name__ == '__main__':
    app.run(debug=True, port=8000)