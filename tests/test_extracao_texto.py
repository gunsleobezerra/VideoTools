import unittest
import os, sys
from videotools.converter import *
from videotools.chunks import *
from videotools.transcribe import *

class TestChunks(unittest.TestCase):
    
    #printando path
    print(os.path.relpath("./teste.mp4"))

    #setup

    def test_dividir_chunks(self):
        self.assertNotEqual(makeChunks(os.path.relpath('tests/teste.wav')),None)


class TestGeracaodeTexto(unittest.TestCase):
        
        #printando path
        print(os.path.relpath("./teste.mp4"))
    
        #setup
    
        def test_transcricao_unitaria(self):
            text=""""""
            chunkpath = os.path.relpath("./chunks")
            chunklist = os.listdir(os.path.relpath("./chunks"))
            for sound in chunklist[:1]:
                text+="\n"+transcreve_audio(os.path.join(chunkpath,sound))
            #write text to file
            with open(os.path.relpath("tests/transcricao.txt"),"w") as f:
                #write using utf-8
                f.write(text)
            self.assertNotEqual(text,"")
            ...
        
        def test_gera_texto_completo(self):
            with open(os.path.relpath("tests/transcricaoCOMPLETA.txt"),"w") as f:
                #write using utf-8
                f.write(geratexto(os.path.relpath("./chunks")))
             
            pass

    

if __name__ == '__main__':
    unittest.main()