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
        self.assertNotEqual(makeChunks(os.path.relpath('tests/teste.wav'),chunk_size=30000),None)


class TestGeracaodeTexto(unittest.TestCase):
        
        #printando path
        print(os.path.relpath("./teste.mp4"))
    
        #setup
    
        def test_transcricao(self):
            text=""""""
            chunkpath = os.path.relpath("./chunks")
            chunklist = os.listdir(os.path.relpath("./chunks"))
            for sound in chunklist:
                text+=transcreve_audio(os.path.join(chunkpath,sound))
            #write text to file
            with open("transcricao.txt","w") as f:
                f.write(text)
            self.assertNotEqual(text,"")
            ...

    

if __name__ == '__main__':
    unittest.main()