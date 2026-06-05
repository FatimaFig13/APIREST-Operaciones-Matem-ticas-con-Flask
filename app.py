from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['GET'])
def suma():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a + b
        return jsonify({"operacion": "suma", "a": a, "b": b, "resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Parámetros inválidos. Usa números en 'a' y 'b'"}), 400

@app.route('/resta', methods=['GET'])
def resta():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a - b
        return jsonify({"operacion": "resta", "a": a, "b": b, "resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Parámetros inválidos. Usa números en 'a' y 'b'"}), 400

@app.route('/multiplicacion', methods=['GET'])
def multiplicacion():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a * b
        return jsonify({"operacion": "multiplicacion", "a": a, "b": b, "resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Parámetros inválidos. Usa números en 'a' y 'b'"}), 400

@app.route('/division', methods=['GET'])
def division():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "No se puede dividir entre cero"}), 400
        resultado = a / b
        return jsonify({"operacion": "division", "a": a, "b": b, "resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Parámetros inválidos. Usa números en 'a' y 'b'"}), 400


@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        datos = request.get_json()
        a = float(datos['a'])
        b = float(datos['b'])
        operacion = datos['operacion']  

        if operacion == 'suma':
            resultado = a + b
        elif operacion == 'resta':
            resultado = a - b
        elif operacion == 'multiplicacion':
            resultado = a * b
        elif operacion == 'division':
            if b == 0:
                return jsonify({"error": "No se puede dividir entre cero"}), 400
            resultado = a / b
        else:
            return jsonify({"error": f"Operación '{operacion}' no válida"}), 400

        return jsonify({"operacion": operacion, "a": a, "b": b, "resultado": resultado})

    except (TypeError, ValueError, KeyError):
        return jsonify({"error": "JSON inválido. Envía: {'a': num, 'b': num, 'operacion': str}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
