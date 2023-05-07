import speech_recognition as sr
import pyttsx3
from datetime import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'tina' in comando:
                print(comando)
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone está desabilitado')
        
    return comando

def comando_de_voz():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são'+hora)
        maquina.runAndWait()
        
comando_de_voz()
        
 