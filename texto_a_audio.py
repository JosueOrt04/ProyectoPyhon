from gtts import gTTS
import os
import time

def texto_a_audio():
    # Crear la carpeta "audios" 
    carpeta_audios = "audios"
    if not os.path.exists(carpeta_audios):
        os.makedirs(carpeta_audios)

    while True:
        texto = input("Introduce el texto que deseas convertir a audio (o escribe 'salir' para terminar): ")

        if texto.lower() == "salir":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if not texto.strip():
            print("El texto está vacío. Por favor, introduce algo.")
            continue

        try:
            # Crear un nombre de archivo único usando la marca de tiempo
            timestamp = int(time.time())
            archivo = os.path.join(carpeta_audios, f"audio_{timestamp}.mp3")

            # Convertir texto a audio y guardar el archivo
            tts = gTTS(text=texto, lang='es')
            tts.save(archivo)
            print(f"Audio generado y guardado en: {archivo}")

        except Exception as e:
            print(f"Ocurrió un error al generar el audio: {e}")

if __name__ == "__main__":
    texto_a_audio()
