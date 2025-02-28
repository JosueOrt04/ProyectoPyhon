from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os
import time

app = Flask(__name__)

# Crear la carpeta "audios" si no existe
carpeta_audios = "audios"
if not os.path.exists(carpeta_audios):
    os.makedirs(carpeta_audios)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/convert", methods=["POST"])
def convert_text_to_speech():
    data = request.get_json()
    texto = data.get("texto", "")

    if not texto.strip():
        return jsonify({"error": "El texto está vacío"}), 400

    try:
        # Crear un nombre de archivo único usando la marca de tiempo
        timestamp = int(time.time())
        archivo = os.path.join(carpeta_audios, f"audio_{timestamp}.mp3")

        # Convertir texto a audio y guardar el archivo
        tts = gTTS(text=texto, lang="es")
        tts.save(archivo)

        return send_file(archivo, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
