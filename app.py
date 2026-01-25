from flask import Flask, jsonify, request
app = Flask(__name__)

# Ruta 1: Health Check (Para saber si el servidor está vivo)
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "service": "credit-risk-api"})

# Ruta 2: La predicción (Simulada por ahora)
@app.route('/predict', methods=['POST'])
def predict():
    # Aquí recibiríamos los datos del cliente
    data = request.get_json()

    # ... Aquí iría la magia de tu modelo ...

    # Devolvemos una respuesta JSON
    return jsonify({
        "mensaje": "Datos recibidos",
        "prediccion_ficticia": 0.85,
        "input_recibido": data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)