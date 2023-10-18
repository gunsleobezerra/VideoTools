import unittest
import os, sys
from videotools.converter import *
from videotools.chunks import *

class TestChunks(unittest.TestCase):
    
    #printando path
    print(os.path.relpath("./teste.mp4"))

    #setup

    def test_dividir_chunks(self):
        self.assertNotEqual(makeChunks(os.path.relpath('tests/teste.wav')),None)

   

    

if __name__ == '__main__':
    unittest.main()