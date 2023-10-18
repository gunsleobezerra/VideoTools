import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from tqdm import tqdm
import os, sys


def transcreve_audio(audio_name:str):
  r = sr.Recognizer()
  with sr.AudioFile(audio_name) as source:
    audio = r.record(source)  
  try:
    texto = r.recognize_google(audio,language='pt-BR')
    print('Google Speech Recognition: ' + texto)
  except sr.UnknownValueError:
    texto = ''
    print('Google Speech Recognition NÃO ENTENDEU o audio')
  except sr.RequestError as e:
    texto = ''
    print('Erro ao solicitar resultados do Google Speech Recognition; {0}'.format(e))
  finally:
    try:
        os.remove(audio_name)
    except:
        print('Arquivo não existe')    
  return texto