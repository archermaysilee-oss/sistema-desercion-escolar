import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cargar el modelo entrenado previamente
with open('modelo_desercion.pkl', 'rb') as f:
    modelo = pickle.load(f)

@app.route('/api/v1/predict', methods=['POST'])
def predecir():
    try:
        datos = request.get_json()
        
        features = np.array([[
            datos.get('promedio', 0.0),
            datos.get('asistencias', 0.0),
            datos.get('nivel_socioeconomico', 1),
            datos.get('materias_reprobadas', 0)
        ]])
        
        prediccion = modelo.predict(features)
        probabilidad = modelo.predict_proba(features)
        
        resultado = {
            "riesgo_desercion": int(prediccion[0]),
            "probabilidad": float(np.max(probabilidad))
        }
        
        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
