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
import pynormalize

parser = argparse.ArgumentParser(description="extract video from youtube, convert to mp3, and combine with pre/post bumpers")
parser.add_argument('-u', '--url', type=str, help="url to youtube video", required=True)
parser.add_argument('-os', '--offset_start', type=int, help="start X seconds into audio, eg: --offset_start 60")
#parser.add_argument('-t', '--truncate', type=int, help="truncate the file by X seconds, eg --truncate 60")
parser.add_argument('-c', '--combine', action='store_true', help="Combine Bumpers to create a FINAL-filename.mp3")
group = parser.add_mutually_exclusive_group()
group.add_argument('-n', '--normalize', action='store_true', help='Normalize audio volumes using ffmpeg libraries')
group.add_argument('-bn', '--bignormalize', action='store_true', help='Normalize big file')
parser.add_argument('-d', '--dbfs', type=float, help='optional setting for normalize, sets "target dialogue normalization fill scale", defaults to 0, -13.5 seems to work well too. I don\'t really know what this is doing, but you can look at the ffmpeg documentation, or just try a bunch of numbers and see what works.')


args=parser.parse_args()

def combine_bumpers(audioname, outPutFile):
    outfile = open(outPutFile, "wb")

    for file in ("pre.mp3", audioname, "post.mp3"):
        f=open(file, "rb")
        outfile.write(f.read())
        f.close
    
    outfile.close
    return True

if args.dbfs is not None and args.normalize is None:
    message = "you must use -n/--normalize when specifiying the dbfs, otherwise it doesn't make sense."
    raise Exception(message)
    str(message)

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
    outPutFile = "FINAL-" + audioname
    combine_bumpers(audioname, outPutFile)
else:
    outPutFile = audioname

if args.normalize is True:
    Files = [outPutFile]
    #target_dbfs = -13.5
    if args.dbfs is None:
        dbfs=0
    else:
        dbfs=args.dbfs

    pynormalize.process_files(Files, -13.5)

   # pynormalize.process_files(
        #Audio=Files,
     #   Audio=outPutFile
    #   target_dbfs=target_dbfs,
    #)

if args.bignormalize is True:
    cmd =  'ffmpeg-normalize "' + outPutFile + '" -o "NORMALIZED\\' + outPutFile + '" -c:a mp3'
    os.system(cmd)

    