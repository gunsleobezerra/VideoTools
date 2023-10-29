import unittest
import os, sys
from pytube import YouTube

class TestYoutbe(unittest.TestCase):
    
    #printando path
    print(os.path.relpath("./teste.mp4"))

    #setup
    def SetUp(self):
        if not os.path.exists("source/youtube"):
            os.makedirs("source/youtube")
        
        

    def test_download(self):
       #video https://www.youtube.com/watch?v=D_0R9e6hqVs
       
        yt = YouTube("https://www.youtube.com/watch?v=D_0R9e6hqVs")

       
        d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        #RENAME
        

        SAVE_PATH = os.path.relpath("source/youtube")

        d_video.download(SAVE_PATH, filename="teste.mp4")

        self.assertNotEqual(d_video,None)
        


    
    

if __name__ == '__main__':
    unittest.main()