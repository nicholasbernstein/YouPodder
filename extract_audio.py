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
import argparse

parser = argparse.ArgumentParser(description="extract video from youtube, convert to mp3, and combine with pre/post bumpers")
parser.add_argument('-u', '--url', type=str, help="url to youtube video", required=True)
parser.add_argument('-os', '--offset_start', type=int, help="start X seconds into audio, eg: --offset_start 60")
#parser.add_argument('-t', '--truncate', type=int, help="truncate the file by X seconds, eg --truncate 60")
parser.add_argument('-c', '--combine', action='store_true', help="Combine Bumpers to create a FINAL-filename.mp3")

args=parser.parse_args()

def combine_bumpers(audioname):
    outPutFile = "FINAL-" + audioname
    outfile = open(outPutFile, "wb")

    for file in ("pre.mp3", audioname, "post.mp3"):
        f=open(file, "rb")
        outfile.write(f.read())
        f.close
    
    outfile.close
    return True

cwd = os.getcwd()
#url = sys.argv[1]
#yt = pytube.YouTube(url)

yt = pytube.YouTube(args.url)
stream = yt.streams.first()
stream.download()
name = stream.default_filename

# Check to see if there is an offset on the command line and if there is, use it.
if args.offset_start is None:
    offset = 0
else: 
    offset = args.offset_start


# Check to see if there is an offset on the command line and if there is, use it.
#if args.truncate is None:
#    truncate = 0
#else: 
#    truncate = args.truncate

#use moviepy to create a clip, with the optinal offset/truncate
#clip = mp.VideoFileClip(name).subclip(offset, truncate) 
clip = mp.VideoFileClip(name).subclip(offset)

#Extract the audio and write to a file
audioname = re.sub(r"\.mp4$", ".mp3", name)
clip.audio.write_audiofile(audioname)

if args.combine is True:
    combine_bumpers(audioname)
