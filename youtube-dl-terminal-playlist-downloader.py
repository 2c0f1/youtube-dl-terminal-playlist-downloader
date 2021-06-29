import os

while True:
 print ('entre com a url do youtube:')
 url_youtube = input()
 path = os.chdir('/home/user/Downloads/Music')
 x = os.popen('youtube-dl --yes-playlist --extract-audio --audio-format mp3 '+url_youtube)
 output = x.readlines()
 print ('convertido para mp3')
