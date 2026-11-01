# Sistema Inteligente de Predicción y Prevención Temprana de Deserción Escolar

Este proyecto implementa una solución técnica completa y desplegable basada en Aprendizaje Automático para la detección temprana de estudiantes en riesgo de deserción escolar.

## 🚀 Arquitectura del Proyecto

El sistema está dividido en dos componentes principales:

- **Backend:** API REST construida con Flask y Python que procesa los datos del alumno mediante un modelo previamente entrenado (`modelo_desercion.pkl`).
- **Frontend:** Interfaz web interactiva (HTML/JS) que permite consultar el nivel de riesgo en tiempo real.

## 🛠️ Tecnologías Utilizadas

- Python 3.9
- Flask / Gunicorn
- Scikit-learn
- Docker
- HTML5 / JavaScript (ES6)

## 📋 Endpoints de la API

### Evaluar Riesgo de Deserción
- **Ruta:** `/api/v1/predict`
- **Método:** `POST`
- **Cuerpo de la solicitud (JSON):**
  ```json
  {
    "promedio": 7.5,
    "asistencias": 85.0,
    "nivel_socioeconomico": 2,
    "materias_reprobadas": 1
  }{
  "riesgo_desercion": 1,
  "probabilidad": 0.88
