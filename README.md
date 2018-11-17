# This program will download a video from youtube using it's URL
# It will then create a mp3 version of the file
# Lastly it will add "bumpers" to the mp3 and save it as out.mp3 

----------------------
Installing
----------------------
[1] PYTHON
# Download & install python 3.7 or later from python.org (probably works with other versions, but 3.7 was tested)

[2] FFMPEG
# Download and install the ffmpeg program for your operating system from ffmpeg.org
# extract the zip file and copy the programs in the "bin" directory to the directory this program is in. 
# The FFMPEG programs are distributed under the LGPL license: http://ffmpeg.org/legal.html

[3] MODULES
# Run the following commmands in a terminal/command prompt to install required python modules:
# (modules only need to be installed the first time)

pip install -r requirements.txt

----------------------
Running the command
----------------------

# Copy two mp3 files to the directory where this script is located.
# call one pre.mp3
# call the other post.mp3

# Once you have installed the modules: 

Run the command: "cd path"
	- where path is the path to the folder this program is in (eg: c:\YouPodder\ or ~/Downloads/YouPodder)
	- on mac systems you can drag the folder onto the terminal and that will insert the path

run the command: 	

usage: extract_audio.py [-h] -u URL [-os OFFSET_START] [-c] [-n | -bn]
                        [-d DBFS]

extract video from youtube, convert to mp3, and combine with pre/post bumpers

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     url to youtube video
  -os OFFSET_START, --offset_start OFFSET_START
                        start X seconds into audio, eg: --offset_start 60
  -c, --combine         Combine Bumpers to create a FINAL-filename.mp3
  -n, --normalize       Normalize audio volumes using ffmpeg libraries
  -bn, --bignormalize   Normalize big file
  -d DBFS, --dbfs DBFS  optional setting for normalize, sets "target dialogue
                        normalization fill scale", defaults to 0, -13.5 seems
                        to work well too. I don't really know what this is
                        doing, but you can look at the ffmpeg documentation,
                        or just try a bunch of numbers and see what works.

