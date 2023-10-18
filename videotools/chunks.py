from pydub import AudioSegment
from pydub.utils import make_chunks
from tqdm import tqdm
import os

timechunk = 30000

def makeChunks(arquivo:str,destino:str=".",chunk_size:int=timechunk,destinoNome:str="./chunks"):
    #pegar o nome do arquivo sem a pasta
    nomeArquivo = arquivo
    print("Dividindo arquivo em chunks de ",chunk_size,"ms...")
    # Check if file exists
    if not os.path.exists(arquivo):
        raise FileNotFoundError("Arquivo não encontrado: " + arquivo)
    #pydub
    clip = AudioSegment.from_wav(os.path.realpath(arquivo))
    chunks = make_chunks(clip, chunk_size)

    #apaga todos os arquivos da pasta
    try:
        for file in os.listdir(destinoNome):
            os.remove(os.path.join(destinoNome,file))
    except:
        pass
    if not os.path.exists(destinoNome):
        os.makedirs(destinoNome)



    time=0
    # Export all of the individual chunks as wav files
    for i, chunk in tqdm(enumerate(chunks)):
        
        chunk_name = os.path.join(destinoNome,f"_chunk_ms_{time}.wav".format(i))
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")
        time+=chunk_size
    print("Arquivo dividido com sucesso!")
    return chunks