import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from tqdm import tqdm
import os, sys

def makeChunks(arquivo:str,destino:str=".",chunk_size:int=30000,destinoNome:str="./chunks"):
    #pegar o nome do arquivo sem a pasta
    nomeArquivo = arquivo
    print("Dividindo arquivo em chunks de ",chunk_size,"ms...")
    # Check if file exists
    if not os.path.exists(arquivo):
        raise FileNotFoundError("Arquivo não encontrado: " + arquivo)
    #pydub
    clip = AudioSegment.from_wav(os.path.realpath(arquivo))
    chunks = make_chunks(clip, chunk_size)

    if not os.path.exists(destinoNome):
        os.makedirs(destinoNome)

    # Export all of the individual chunks as wav files
    for i, chunk in tqdm(enumerate(chunks)):
        chunk_name = os.path.join(destinoNome,"_chunk{0}.wav".format(i))
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")
    print("Arquivo dividido com sucesso!")
    return chunks