#By Dx55

from __future__ import unicode_literals
import youtube_dl
import urllib.request
import urllib.parse
import re

while True:
    name = input("Enter the name\n")
    
    print("Wait...")
    
    query_string = urllib.parse.urlencode({"search_query" : name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    result = ("http://www.youtube.com/watch?v=" + search_results[0])
    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors':
    [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([result])
    
    if input("Another one? (y/n)\n") == 'n':
        break
