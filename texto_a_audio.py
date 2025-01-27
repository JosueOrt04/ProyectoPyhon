from gtts import gTTS
import os

def texto_a_audio():
    while True:
        # Pedir al usuario que ingrese el texto
        texto = input("Introduce el texto que deseas convertir a audio (o escribe 'salir' para terminar): ")

        if texto.lower() == "salir":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        # Verificar si el texto no está vacío
        if not texto.strip():
            print("El texto está vacío. Por favor, introduce algo.")
            continue

        # Convertir texto a audio
        try:
            tts = gTTS(text=texto, lang='es')  # 'es' indica español
            archivo = "audio_generado.mp3"
            tts.save(archivo)
            print(f"Audio generado y guardado como {archivo}")

            # Reproducir el archivo de audio 
            os.system(f"mpg123 {archivo}")
        except Exception as e:
            print(f"Ocurrió un error al generar el audio: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    texto_a_audio()
