import pyttsx3
import os
import time

def texto_a_audio():
    carpeta_audios = "audios"
    if not os.path.exists(carpeta_audios):
        os.makedirs(carpeta_audios)

    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # Ajusta la velocidad de habla

    while True:
        texto = input("Introduce el texto que deseas convertir a audio (o escribe 'salir' para terminar): ")

        if texto.lower() == "salir":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if not texto.strip():
            print("El texto está vacío. Por favor, introduce algo.")
            continue

        try:
            timestamp = int(time.time())
            archivo = os.path.join(carpeta_audios, f"audio_{timestamp}.mp3")

            engine.save_to_file(texto, archivo)
            engine.runAndWait()  # Procesa el audio rápido
            print(f"Audio generado en: {archivo}")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    texto_a_audio()
