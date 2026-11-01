async function enviarDatos() {
    const data = {
        promedio: parseFloat(document.getElementById('promedio').value),
        asistencias: parseFloat(document.getElementById('asistencias').value),
        nivel_socioeconomico: 2,
        materias_reprobadas: parseInt(document.getElementById('materias_reprobadas').value)
    };

    try {
        const response = await fetch('http://localhost:5000/api/v1/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        
        const mensaje = result.riesgo_desercion === 1 
            ? "⚠️ Alerta: Alto Riesgo de Deserción" 
            : "✅ Alerta: Estudiante Estable";
            
        document.getElementById('resultado').innerText = `${mensaje} (Confianza: ${(result.probabilidad * 100).toFixed(1)}%)`;
    } catch (error) {
        document.getElementById('resultado').innerText = "Error al conectar con el servidor.";
    }
}
