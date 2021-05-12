import requests
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import sys
# audio_downloader.extract_info('https://www.youtube.com/watch?v=3XM023yz_pI')
# spotify playlist url
# url = 'https://open.spotify.com/playlist/61OHJQz4J2xsDYJsOt5TVP'


def yt_url(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ','+')}"
    r = requests.get(url).text.split('i.ytimg.com/vi/')[1].split('/')[0]
    return f'https://www.youtube.com/watch?v={r}'


def get_spotify_track_names(url):
    r = requests.get(url)
    trakcs = []
    soup = BeautifulSoup(r.content, 'lxml')
    for track in soup.find_all('span', {'class': 'track-name'}):
        artist = track.parent.a.span.text
        trakcs.append(f"{track.text} {artist}")
    return trakcs


if __name__ == '__main__':
    for track in get_spotify_track_names(sys.argv[1]):
        audio_downloader = YoutubeDL({'format': 'm4a'})
        audio_downloader.extract_info(yt_url(track))
