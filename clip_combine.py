#################################################################################
# this program takes the name of an audio file                                  #
# and then combines pre.mp3 <file> post.mp3 into a new file called FINAL-file   #
# hastely written by nick@nicholasbernstein.com                                 #
#################################################################################

import sys
myFile = sys.argv[1]
outPutFile = "FINAL-" + myFile

outfile = open(outPutFile, "wb")

for file in ("pre.mp3", myFile, "post.mp3"):
    f=open(file, "rb")
    outfile.write(f.read())
    f.close
    
outfile.close    