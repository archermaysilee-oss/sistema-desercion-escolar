import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cargar el modelo de machine learning de deserción escolar
try:
    with open('modelo_desercion.pkl', 'rb') as f:
        modelo = pickle.load(f)
except Exception as e:
    modelo = None
    print(f"Advertencia: No se pudo cargar el modelo: {e}")

@app.route('/')
def home():
    return jsonify({"estado": "API de Predicción de Deserción Escolar Activa"})

@app.route('/predecir', methods=['POST'])
def predecir():
    if modelo is None:
        return jsonify({"error": "El modelo no está disponible"}), 500
    data = request.get_json()
    # Aquí puedes ajustar las características según tu modelo
    caracteristicas = np.array(data.get('features')).reshape(1, -1)
    prediccion = modelo.predict(caracteristicas)
    return jsonify({"prediccion": int(prediccion[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
