Manual de Despliegue en la Nube - Sistema Inteligente de Predicción y Prevención Temprana de Deserción Escolar
Este manual detalla los procedimientos técnicos, la estructura de la aplicación en Flask y los pasos necesarios para desplegar el modelo predictivo de deserción escolar utilizando contenedores Docker en un entorno de producción o nube.
1. Arquitectura del Sistema y Componentes
El proyecto se compone de un backend basado en Python/Flask que expone un servicio REST para realizar inferencias en tiempo real utilizando un modelo de Machine Learning preentrenado (modelo_desercion.pkl).
app.py: Servidor API Flask con endpoints para comprobación de estado y predicción.
Dockerfile: Receta de contenedorización basada en Python para empaquetar dependencias y el modelo.
requirements.txt: Listado estricto de librerías requeridas (flask, scikit-learn, pandas, gunicorn, etc.).
modelo_desercion.pkl: Artefacto serializado del modelo de Machine Learning.
2. Requisitos Previos
Antes de realizar el despliegue en cualquier servidor en la nube (AWS, GCP, Azure, Render o Heroku), asegúrate de contar con:
Docker instalado y en ejecución en la máquina host o servidor de destino.
Acceso a la terminal o consola de comandos.
Imagen o entorno compatible con contenedores Linux/x86_64.
3. Pasos de Despliegue Local y en Contenedor (Docker)
* Paso 1: Clonar el Repositorio
Bash
git clone https://github.com/archermaysilee-oss/sistema-desercion-escolar.git
cd sistema-desercion-escolar/backend
* Paso 2: Construir la Imagen Docker
Ejecuta el siguiente comando dentro de la carpeta backend para generar la imagen del contenedor:
Bash
docker build -t desercion-backend .
Verificación: La terminal debe mostrar la compilación exitosa de cada una de las capas de dependencias de Python indicando Successfully built.
* Paso 3: Ejecutar el Contenedor en Producción
Despliega el contenedor mapeando el puerto 5000 del servidor al puerto 5000 de la aplicación:
Bash
docker run -d -p 5000:5000 --name contenedor-desercion desercion-backend
Verificación: Ejecuta docker ps y verifica que el contenedor contenedor-desercion aparezca en estado Up.
4. Endpoints y Verificación del Servicio
Una vez que el servicio esté corriendo en la nube o en tu servidor local, puedes verificar su funcionamiento mediante peticiones HTTP:
A. Verificación de Estado (Health Check)
Método: GET
Ruta: /
Comando de prueba:
Bash
curl http://localhost:5000/
Respuesta esperada:
JSON
{"estado": "API de Predicción de Deserción Escolar Activa"}
B. Inferencia de Predicción
Método: POST
Ruta: /predecir
Comando de prueba:
Bash
curl -X POST http://localhost:5000/predecir \
     -H "Content-Type: application/json" \
     -d '{"caracteristicas": [/* valores numéricos del estudiante */]}'
Respuesta esperada:
JSON
{"prediccion": 0}
5. Consideraciones de Seguridad y Mantenimiento
Escalabilidad: Se recomienda utilizar un orquestador como Kubernetes o servicios gestionados de contenedores (como AWS ECS o Google Cloud Run) para manejar cargas concurrentes altas.
Monitoreo: Configurar alertas sobre los logs del contenedor (docker logs contenedor-desercion) para det
