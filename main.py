import datetime
import os, sys
import pprint
from videotools.converter import *
import videotools.chunks as chunks
from videotools.transcribe import *
from videotools.talkgpt import *
from videotools.download_video import *
import os
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import argparse
from multiprocessing import Pool

def main(args_videotools):

    parser = argparse.ArgumentParser(description='VideoTools Arguments')
    print("\n\n"+get_completion("Repita 'Eu estou funcionando e sou o GPT' : ")+"\n\n")
    

    #convertendo de mp4 para mp3
    # videoMp4=args[1]
    parser.add_argument('-videoMp4','-v', type=str, help='video path')
    
    # destino=args[2]
    parser.add_argument('-destino','-d', type=str, help='destination path')
    parser.add_argument('-leng','-lg', type=str, help='language')
    parser.add_argument('-timechunk','-tc', type=int, help='timechunk')
    parser.add_argument('-assuntos','-as', type=int, help='Number of subjects')
    parser.add_argument('-url','-u', type=str, help='url')

    args_videotools = parser.parse_args()

    print(args_videotools.videoMp4)

    videoMp4=args_videotools.videoMp4
    destino=args_videotools.destino

    #baixa video do youtube se tiver url
    if args_videotools.url:
        #filename video_name_date
        date_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_name = "video_"+str(date_now)
        print(args_videotools.url)
        print(video_name)
        dowload_youtube(args_videotools.url,video_name,destino)
        print("baixou!")
        videoMp4=os.path.join(destino,video_name+".mp4")
    else:
        video_name = os.path.splitext(videoMp4)[0]
        video_name = video_name.split("/")[-1]

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

    converter(videoMp4,"mp4","mp3", os.path.relpath(destino))

    ARQUIVO_MP3 = os.path.join(destino,video_name+".mp3")
    leng_no_=leng.split("-")[0]
    transcribe_py=os.path.realpath("videotools/transcribe.py")
    os.system(f"python3 {transcribe_py} -mp3 {ARQUIVO_MP3} -lang {leng_no_} > {os.path.join(destino,'transcricao.txt')}")

    print("transcrição completa!! -- "+os.path.join(destino,'transcricao.txt'))

    with open(os.path.join(destino,"transcricao.txt"),"r") as f:
        texto=f.read()
        texto.split("INICIANDO TRANSRIÇÃO:")[1].split("TERMINANDO TRANSCRIÇÃO---")[0]

    #gerando assuntos
    we_got_it=False

    while(not we_got_it):
        a_geracao=gerar_assuntos(texto,destino,subjects,leng)
        b_geracao=gerar_assuntos(a_geracao,destino,subjects,leng)
        
        
        

        #obtendo cortes
        # [00:07.660 | 01:10.440] - Elogio e comentário sobre o livro de Vardin Rogovim e evento em Belo Horizonte.
        # [01:10.440 | 03:09.500] - Discussão sobre a história do movimento comunista no Brasil e a influência do Stalinismo.
        # [03:09.500 | 05:08.040] - Exploração do impacto histórico e político do Stalinismo na União Soviética, ressaltando a obra de Vadim Rogovim.
        # [05:08.040 | 06:58.020] - Análise crítica do surgimento e efeitos do Stalinismo na história soviética e na tradição marxista.
        # [06:58.020 | 16:53.540] - Detalhes sobre o conteúdo e a importância da obra de Rogovim, além de convite para o evento em Belo Horizonte e considerações finais.
        cortes=[]
        clip=[]
        try:
            with open(os.path.join(destino,"cortes.txt"),"r") as f:
                linhas=f.readlines()
                for linha in linhas:
                    try:
                        clip={"t_inicial":linha.split("|")[0].split("[")[1].split("]")[0].strip(),"t_final":linha.split("|")[1].split("]")[0].strip(),"assunto":linha.split("|")[1].split("]")[1].strip()}
                    except:
                        pass
                    cortes.append(clip)
                print("CONSEGUIU OS CORTES:")
                print(cortes)

            
            #cortando videos e gerando clips na pasta [destino]/clips
            print("CORTANDO VIDEOS E GERANDO CLIPS NA PASTA [destino]/clips")
            video = mp.VideoFileClip(videoMp4)
            if not os.path.exists(os.path.join(destino,"clips")):
                os.makedirs(os.path.join(destino,"clips"))
            for corte in cortes:
                try:
                    
                    if(corte["t_inicial"]!="t_inicial" and corte["t_final"]!="t_final"):
                       
                        get_Segundos = lambda x: float(x.split(":")[0])*60+float(x.split(":")[1].split(".")[0])+float(x.split(":")[1].split(".")[1])/1000
                        t_inicial=corte["t_inicial"]
                        t_final=corte["t_final"]
                        #coloca os tempos no padrão 00:00:00.00
                        if(len(t_inicial.split(":"))==2):
                            t_inicial="00:"+t_inicial
                        

                        print(f"Cortando de {t_inicial} até {t_final} -  clip: {corte['assunto']}")
                        
                        clip = video.subclip(t_inicial,t_final)
                        #nome do arquivo encodeado para tirar caracteres especiais
                        nome_arquivo=corte["assunto"].encode('ascii', 'ignore').decode('ascii')
                        #tira todos os caracteres especiais
                        nome_arquivo = ''.join(e for e in nome_arquivo if e.isalnum() or e==" ")


                        nome_clip=os.path.join(destino,"clips",nome_arquivo.replace(" ","_")+".mp4")
                        
                        #utilizando multiprocessing para cortar os videos
                        clip.write_videofile(nome_clip,codec="libx264",threads=4)
                        
            
                except Exception as e:
                    print("\n\nerro ao cortar o video : "+corte["assunto"]+"\n\n")
                    print(e)
                    continue
            print("CORTES COMPLETOS!!")
            we_got_it=True
        except Exception as e:
            print("erro ao obter os cortes, tente novamente: "+str(e))
            we_got_it=False
        
    ...

def gerar_assuntos(transcricao:str,destino:str,subjects:int,leng:str,max_length:int=200):
    #obtendo cortes

    #contando linhas da transcrição
    linhas = transcricao.split("\n")
    respostaFinal=""
    
    

    for i in range(0,len(linhas),max_length):
        #obtendo a parte
        parte = linhas[i:i+max_length]
        #escrevendo em um arquivo
        with open(os.path.join(destino,"transcricao.txt"),"w") as f:
            f.write("\n".join(parte))
        #gerando assuntos
        

        with open(os.path.join(destino,"transcricao.txt"),"r") as f:
            texto=f.read()

            resposta=""

            

            while(resposta==""):
                resposta =get_completion(f"""
                Leia a transcrição abaixo e SUMARIZE EM POUCAS PALAVRAS ({subjects} assuntos) retornando EXATAMENTE [t_inicial | t_final ] -  [Assunto]
                
                transcrição:
                                {texto}

                LEMBRE-SE DE RETORNAR EXATAMENTE NO PADRÃO [t_inicial | t_final ] -  [Assunto] E EM {leng}!
                POIS EU VOU PEGAR OS CORTES USANDO ESSA EXPRESSÃO: "t_inicial":linha.split("|")[0].split("[")[1].split("]")[0].strip(),"t_final":linha.split("|")[1].split("]")[0].strip(),"assunto":linha.split("|")[1].split("]")[1].strip()
                """)
                print("Resposta"+resposta)

            respostaFinal+=resposta+"\n"

            #tirar linhas em branco
            

        
        
    
    with open(os.path.join(destino,"cortes.txt"),"w") as f:
        f.write(respostaFinal)
    return respostaFinal

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))