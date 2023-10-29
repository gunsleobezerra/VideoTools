from asyncio import exceptions
from pytube import YouTube
import os, sys

def dowload_youtube(url:str, filneame:str, path:str,extension:str="mp4"):
    yt = YouTube(url)
    print("Baixando de "+url)
    try:
        d_video =yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first()

        #RENAME
        

        SAVE_PATH =  os.path.relpath(path)

    
        d_video.download(SAVE_PATH, filename=filneame+"."+extension)
    except Exception as e:
        print(f"Erro ao baixar video: {e} ")
        sys.exit(1)

    