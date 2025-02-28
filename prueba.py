from gtts import gTTS
import os
import time
from pydub import AudioSegment

def generar_audiolibro(archivo_texto, idioma='es'):
    carpeta_audios = "audios"
    audiolibro_final = "audiolibro.mp3"

    # Crear carpeta si no existe
    if not os.path.exists(carpeta_audios):
        os.makedirs(carpeta_audios)

    try:
        # Leer el archivo de texto
        with open(archivo_texto, "r", encoding="utf-8") as file:
            texto = file.read()

        # Dividir el texto en partes de máximo 500 caracteres para evitar errores
        partes = [texto[i:i+500] for i in range(0, len(texto), 500)]
        
        audios_generados = []
        
        for i, parte in enumerate(partes):
            archivo_audio = os.path.join(carpeta_audios, f"parte_{i}.mp3")
            tts = gTTS(text=parte, lang=idioma)
            tts.save(archivo_audio)
            audios_generados.append(archivo_audio)
            print(f"Generado: {archivo_audio}")

        # Unir los audios en un solo archivo final
        audio_final = AudioSegment.empty()
        for audio in audios_generados:
            audio_segmento = AudioSegment.from_mp3(audio)
            audio_final += audio_segmento
        
        # Guardar el audiolibro final
        ruta_audiolibro = os.path.join(carpeta_audios, audiolibro_final)
        audio_final.export(ruta_audiolibro, format="mp3")
        print(f"Audiolibro generado en: {ruta_audiolibro}")

        # Reproducir el audiolibro
        os.system(f"mpg123 {ruta_audiolibro}")

    except Exception as e:
        print(f"Error al generar el audiolibro: {e}")

if __name__ == "__main__":
    archivo_txt = input("Introduce el nombre del archivo de texto (ejemplo: libro.txt): ")
    if os.path.exists(archivo_txt):
        generar_audiolibro(archivo_txt)
    else:
        print("El archivo no existe. Asegúrate de escribir el nombre correcto.")
