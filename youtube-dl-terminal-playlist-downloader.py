import os
n = ('\n')
while True:
 url_youtube = input('enter the youtube url:'+n)
 print ('baixando')
 path = os.chdir('/home/user/Downloads/Music')
 x = os.popen('youtube-dl --yes-playlist --extract-audio --audio-format mp3 '+url_youtube)
 print(x.read())
 print ('converted to mp3'+n)
