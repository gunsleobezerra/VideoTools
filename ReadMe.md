# VideoTools

## Description
This is a collection of tools for video processing. To cut videos by transcript.

## Before use:

To use this project you need first install ffmpeg video processor library

### linux:
    make install_dependencies (You need install Poetry first)
### windows:
    Download the binaries: https://ffmpeg.org/download.html
    Add the bin Folder to Path: https://phoenixnap.com/kb/ffmpeg-windows

## Usage:
   usage: main.py [-h] [-leng LENG] [-timechunk TIMECHUNK] [-assuntos ASSUNTOS] [-url ]  [-d ] 

    VideoTools Arguments

    positional arguments:
    videoMp4              video path
    destino               destination path

    options:
    -h, --help            show this help message and exit
    -leng LENG, -lg LENG  language
   
    -assuntos ASSUNTOS, -as ASSUNTOS
                            Number of subjects
    -url URL, -u URL      url of video on youtube

