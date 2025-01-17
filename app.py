from flask import Flask, jsonify, request
from flask_cors import CORS
from modulos.limpiar_datos import realizar_pruebas

class ErrorCreator(Exception):
    """
    Clase para crear instancias personalizadas de excepciones, 
    utilizada para gestionar errores específicos durante la creación de protocolos HTTP.

    Attributes:
        error_name (str): Nombre del error.
        message (str): Descripción del error.
    """
    def __init__(self, error_name, message):
        self.error_name = error_name
        self.message = message

    def __str__(self):
        return f'{self.error_name}: {self.message}'



if __name__ != '__main__':
    raise ErrorCreator('ErrorEjecucion', 'Este archivo de python no puede ser ejecutado como un módulo')

app = Flask(__name__)
CORS(app)

@app.route('/ejecutar-pruebas', methods=['POST'])
def enviar_resultados():
    data = request.get_json()
    enlace = data.get('enlace')
    cantidad_peticiones = data.get('cantidad_peticiones')
    concurrencia = data.get('concurrencia')
    cantidad_pruebas = data.get('cantidad_pruebas')

    datos = realizar_pruebas(enlace, int(cantidad_peticiones), int(concurrencia), int(cantidad_pruebas))

    return jsonify(datos)

app.run(debug=True)
