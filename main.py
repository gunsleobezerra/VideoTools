import os, sys
from videotools.converter import *

def main(args):
    #convertendo de mp4 para mp3
    videoMp4=args[1]

    converter(videoMp4,"mp4","mp3")

    ...

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))