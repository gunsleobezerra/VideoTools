import os, sys
from videotools.converter import *
import videotools.chunks as chunks
from videotools.transcribe import *
import os
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks

def main(args):
    #convertendo de mp4 para mp3
    videoMp4=args[1]
    destino=args[2]

    try:
        leng=args[3]
    except:
        leng="pt-BR"
        #ingles: en-US
        #portugues: pt-BR
        #espanhol: es-ES
        #frances: fr-FR
        #italiano: it-IT

    try:
        timechunk=int(args[4])
        print(str(timechunk) + "timechunk")
    except:
        timechunk=30000
        
    #video path example: windows:  "C:\\Users\\User\\Desktop\\video.mp4" linux: "/home/user/video.mp4"

    video_name = os.path.splitext(videoMp4)[0]

    print(video_name)

   

    

    #mp4_to_mp3(videoMp4,destino)
    converter(videoMp4,"mp4","mp3", os.path.relpath(destino))

    #mp3_to_wav(destino,destino)
    converter(os.path.join(destino,"teste.mp3"),"mp3","wav", os.path.relpath(destino))

    #criando chunks
    
    chunks.makeChunks(os.path.join(destino,"teste.wav"),chunk_size=timechunk,destinoNome=os.path.join(destino,"chunks"))

    #transcrevendo

    with open(os.path.join(destino,"transcricao.txt"),"w") as f:
        f.write(geratexto(os.path.join(destino,"chunks"),leng=leng))

    ...

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))