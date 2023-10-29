import os, sys
import pprint
from videotools.converter import *
import videotools.chunks as chunks
from videotools.transcribe import *
from videotools.talkgpt import *
import os
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import argparse

def main(args_videotools):

    parser = argparse.ArgumentParser(description='VideoTools Arguments')

    

    #convertendo de mp4 para mp3
    # videoMp4=args[1]
    parser.add_argument('videoMp4', type=str, help='video path')
    
    # destino=args[2]
    parser.add_argument('destino', type=str, help='destination path')
    parser.add_argument('-leng','-lg', type=str, help='language')
    parser.add_argument('-timechunk','-tc', type=int, help='timechunk')
    parser.add_argument('-assuntos','-as', type=int, help='Number of subjects')
    
    args_videotools = parser.parse_args()

    print(args_videotools.videoMp4)

    videoMp4=args_videotools.videoMp4
    destino=args_videotools.destino

    try:
        # leng=args[3]
        leng=args_videotools.leng if args_videotools.leng else "pt-BR"
    except:
        leng="pt-BR"
        #ingles: en-US
        #portugues: pt-BR
        #espanhol: es-ES
        #frances: fr-FR
        #italiano: it-IT

    try:
        timechunk= args_videotools.timechunk if args_videotools.timechunk else 30000  
        print(str(timechunk) + "timechunk")
    except:
        timechunk=30000

    try:
        subjects= args_videotools.assuntos if args_videotools.assuntos else 3
    except:
        subjects=3

    #video path example: windows:  "C:\\Users\\User\\Desktop\\video.mp4" linux: "/home/user/video.mp4"

    video_name = os.path.splitext(videoMp4)[0]
    video_name = video_name.split("/")[-1]
    print(video_name)

   

    

    #mp4_to_mp3(videoMp4,destino)
    converter(videoMp4,"mp4","mp3", os.path.relpath(destino))

    #mp3_to_wav(destino,destino)
    converter(os.path.join(destino,video_name+".mp3"),"mp3","wav", os.path.relpath(destino))

    #criando chunks
    
    chunks.makeChunks(os.path.join(destino,video_name+".wav"),chunk_size=timechunk,destinoNome=os.path.join(destino,"chunks"))

    #transcrevendo

    with open(os.path.join(destino,"transcricao.txt"),"w") as f:
        f.write(geratexto(os.path.join(destino,"chunks"),leng=leng))
    

    #obtendo cortes
    with open(os.path.join(destino,"transcricao.txt"),"r") as f:
        texto=f.read()

        resposta=""

        while(resposta==""):
            resposta =get_completion(f"""
            Leia a transcrição abaixo e corte os tempos de acordo com o assunto ({subjects} assuntos) retornando [t_inicial | t_final ] -  [Assunto]
             Obs: os assuntos têm que estar em {leng} e não existe intersecção de tempo entre os assuntos
            
            transcrição:
                            {texto}
            """)

    
    with open(os.path.join(destino,"cortes.txt"),"w") as f:
        f.write(resposta)
        
    ...

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))