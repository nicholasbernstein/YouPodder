#################################################################################
# this program takes the url of a youtube video, downloads the mp4 converts     #
# it to mp3
# and then combines pre.mp3 <file> post.mp3 into a new file called FINAL-file   #
# hastely written by nick@nicholasbernstein.com                                 #
#################################################################################

import pytube
import os
import sys
import moviepy.editor as mp
import re


cwd = os.getcwd()
url = sys.argv[1]

yt = pytube.YouTube(url)
stream = yt.streams.first()
stream.download()
name = stream.default_filename

#clip = mp.VideoFileClip(name).subclip(60) #swap this with next line to cut 60 seconds off the beginning
clip = mp.VideoFileClip(name)

audioname = re.sub(r"\.mp4$", ".mp3", name)
#print("\n" + text + "\n")
#audioname = name + ".mp3"

clip.audio.write_audiofile(audioname)

outPutFile = "FINAL-" + audioname

outfile = open(outPutFile, "wb")

for file in ("pre.mp3", audioname, "post.mp3"):
    f=open(file, "rb")
    outfile.write(f.read())
    f.close
    
outfile.close 