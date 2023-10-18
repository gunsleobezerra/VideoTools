import unittest
import os, sys
from videotools.converter import *

class TestConversoes(unittest.TestCase):
    
    #printando path
    print(os.path.relpath("./teste.mp4"))



    def test_mp4_to_mp3(self):
        self.assertNotEqual(converter(os.path.relpath('tests/teste.mp4'),"mp4","mp3"),None)

    def test_mp3_to_wav(self):
        self.assertNotEqual(converter(os.path.relpath('tests/teste.mp3'),"mp3","wav"),None)

    

if __name__ == '__main__':
    unittest.main()