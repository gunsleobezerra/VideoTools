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
    python main.py --help
    usage: main.py [-h] [-leng LENG] [-timechunk TIMECHUNK] videoMp4 destino

    VideoTools Arguments

    positional arguments:
    videoMp4              video path
    destino               destination path

    options:
    -h, --help            show this help message and exit
    -leng LENG, -lg LENG  language
    -timechunk TIMECHUNK, -tc TIMECHUNK
                            timechunk
