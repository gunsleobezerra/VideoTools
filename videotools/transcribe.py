from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from tqdm import tqdm
import os, sys

from .chunks import timechunk

def transcreve_audio(audio_name:str,aditional_args:str="",forGPT:bool=False):
   #windows
  
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
        # if(os.name == 'nt'):
        #     os.system("cls")
        # else:
        #     os.system("clear")
    except:
        print('Arquivo não existe')    
    
    return aditional_args+ texto

def calcula_tempo(MS:int):
    MS = MS/1000
    s = MS%60
    m = (MS//60)%60
    h = (MS//3600)%60
    return f"{int(h)}:{int(m)}:{s}"

# def geratexto(chunks_path:str,chunk_size:int=timechunk,forGPT:bool=False):
   
#     timeMS=0
#     text=""""""
#     text_dict = {}
#     chunklist = os.listdir(chunks_path)
#     total_time = len(chunklist)*chunk_size
#     print(chunklist)
#     #example chunk name : _chunk_ms_147000.wav
#     for sound in chunklist:
#         chunkMS = int(sound.split("_ms_")[1].split(".")[0])

#         text_dict[chunkMS] = transcreve_audio(os.path.join(chunks_path,sound),forGPT=forGPT)
       
#     for i in range(0,total_time,chunk_size):
#         text+=calcula_tempo(i)+" -- "+text_dict[i]+"\n"
#     return text

#multiprocessing

def geratexto(chunks_path:str, chunk_size:int=timechunk, forGPT:bool=False):
    timeMS=0
    text=""""""
    text_dict = {}
    chunklist = os.listdir(chunks_path)
    total_time = len(chunklist)*chunk_size
    print(chunklist)
    #example chunk name : _chunk_ms_147000.wav
    with Pool() as pool:
        results = list(tqdm(pool.imap(transcreve_audio, [os.path.join(chunks_path,sound) for sound in chunklist]), total=len(chunklist)))
        for i, data in enumerate(results):
            chunkMS = int(chunklist[i].split("_ms_")[1].split(".")[0])
            text_dict[chunkMS] = data
       
    print(text_dict)
    # print(text_dict)
    for key in sorted(text_dict.keys()):
        text+= calcula_tempo(key)+" -- "+text_dict[key]+"\n\n"
    return text