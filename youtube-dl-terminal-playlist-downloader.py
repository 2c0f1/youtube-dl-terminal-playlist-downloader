import os

while True:
 print ('enter the youtube url:')
 url_youtube = input()
 path = os.chdir('/home/user/Downloads/Music')
 x = os.popen('youtube-dl --yes-playlist --extract-audio --audio-format mp3 '+url_youtube)
 output = x.readlines()
 print ('converted to mp3')
