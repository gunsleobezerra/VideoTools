# VideoTools

## Description
This is a collection of tools for video processing. To cut videos by transcript.

## Before use:

To use this project you need first install ffmpeg video processor library

### linux:
    sudo apt-get install ffmpeg
### windows:
    Download the binaries: https://ffmpeg.org/download.html
    Add the bin Folder to Path: https://phoenixnap.com/kb/ffmpeg-windows

## Usage:
   usage: main.py [-h] [-leng LENG] [-timechunk TIMECHUNK] [-assuntos ASSUNTOS]
               videoMp4 destino

         [-url ]  -d source -as 5

    VideoTools Arguments

    positional arguments:
    videoMp4              video path
    destino               destination path

    options:
    -h, --help            show this help message and exit
    -leng LENG, -lg LENG  language
    -timechunk TIMECHUNK, -tc TIMECHUNK
                            timechunk
    -assuntos ASSUNTOS, -as ASSUNTOS
                            Number of subjects
    -url URL, -u URL      url of video on youtube

