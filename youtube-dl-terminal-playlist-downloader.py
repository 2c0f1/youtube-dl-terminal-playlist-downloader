import os
import subprocess
n = ('\n')
while True:
 url_youtube = input('enter the youtube url:'+n)
 print ('downloading')
 path = os.chdir('/home/user/Downloads/Music')
 x = subprocess.call('youtube-dl --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --embed-thumbnail '+str(url_youtube),subprocess.PIPE,shell=True)
 out =  x.communicate()
 if '(None, None)' in str(out):
  print ('converted to mp3'+n)
