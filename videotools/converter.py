import os
import subprocess
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks



def converter(arquivo:str,formSource:str,formDest:str,destino:str="."):
    
    #pegar o nome do arquivo sem a pasta
    nomeArquivo = arquivo

    





    if(formSource == "mp4" and formDest == "mp3"):
        print("Convertendo de mp4 para mp3")
        print("Convertendo o arquivo: ",nomeArquivo," de ",formSource," para ",formDest,"...")
    
        try:
            
            #verifica se pasta existe
            if not os.path.exists(destino):
                os.makedirs(destino)

            

            clip = mp.VideoFileClip(arquivo).subclip()
            print("Convertendo...")
            clip.audio.write_audiofile(os.path.join(destino,nomeArquivo.split(".")[0]+"."+formDest))

            print("Arquivo convertido com sucesso!")

            return clip
        except Exception as e:
            print("Erro ao converter arquivo: ",e)
            return None

            
    elif(formSource == "mp3" and formDest == "wav"):
        print("Convertendo o arquivo: ",nomeArquivo," de ",formSource," para ",formDest,"...")
        try:
            # Check if file exists
            if not os.path.exists(arquivo):
                raise FileNotFoundError("Arquivo não encontrado: " + arquivo)
            #pydub
            clip = AudioSegment.from_mp3(os.path.realpath(arquivo))
            print("Convertendo...")
            clip.export(os.path.join(destino,nomeArquivo.split(".")[0]+"."+formDest), format="wav")
            print("Arquivo convertido com sucesso!")
            return clip

            #ffmpeg
            # absoultPath = os.path.abspath(arquivo)
            # print(absoultPath)
            # comamand = ['ffmpeg', '-i', absoultPath, os.path.join(destino,nomeArquivo.split(".")[0]+"."+formDest)]
            # #print comamand
            # for i in comamand:
            #     print(i,end=" ")
            
            # print("\n")


            # subprocess.call(comamand)

            
            


            
            
        

        except FileNotFoundError as e:
            print("Erro ao converter arquivo: ",e)
            return None
        except Exception as e:
            print("Erro ao converter arquivo: ",e)
            return None
        

       
    

    