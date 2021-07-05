import os
n = ('\n')
while True:
 url_youtube = input('entre com a url do youtube:'+n)
 print ('baixando')
 os.chdir('/home/user/Downloads/Music')
 x = os.popen('youtube-dl --yes-playlist --extract-audio --audio-format mp3 '+url_youtube)
 print(x.read())
 print ('convertido para mp3'+n)
