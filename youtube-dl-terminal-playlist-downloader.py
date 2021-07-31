import os
import time
import subprocess
n = ('\n')
while True:
 url_youtube = input('enter the youtube url:'+n)
 print ('downloading')
 path = os.chdir('/home/user/Downloads/Music')
 x = subprocess.call('youtube-dl --yes-playlist --extract-audio --audio-format mp3 '+str(url_youtube), shell=True) 
 time.sleep(20)
 print ('converted to mp3'+n)
 time.sleep(1)
