# By Dx55
import youtube_dl
from youtube_search import YoutubeSearch
import json

while True:
    name = str(input("Enter the name\n"))
    print("Wait...")
    
    results_json = YoutubeSearch(name, max_results=1).to_json()
    results = json.loads(results_json)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for v in results['videos']:
            ydl.download(['http://www.youtube.com/watch?v=' + v['id']])
    
    if input("Another one? (y/n)\n") == 'n':
        break
