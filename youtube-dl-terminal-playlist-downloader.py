import os
import subprocess
n = ('\n')
while True:
 url_youtube = input('enter the youtube url:'+n)
 print ('downloading')
 path = os.chdir('~/Downloads/Music')
 x = subprocess.Popen('yt-dlp -v -c --yes-playlist --playlist-random --embed-thumbnail --extract-audio --audio-format mp3 bestaudio '+str(url_youtube),subprocess.PIPE,shell=True)
 out=x.communicate()
 if '(None, None)' in str(out):
  print ('converted to mp3'+n)
