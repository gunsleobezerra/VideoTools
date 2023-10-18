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

    

    #mp4_to_mp3(videoMp4,destino)
    #converter(videoMp4,"mp4","mp3", os.path.relpath(destino))

    #mp3_to_wav(destino,destino)
    #converter(os.path.join(destino,"teste.mp3"),"mp3","wav", os.path.relpath(destino))

    #criando chunks
    chunks.timechunk = 30000
    chunks.makeChunks(os.path.join(destino,"teste.wav"),destinoNome=os.path.join(destino,"chunks"))

    #transcrevendo

    with open(os.path.join(destino,"transcricao.txt"),"w") as f:
        f.write(geratexto(os.path.join(destino,"chunks")))

    ...

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))