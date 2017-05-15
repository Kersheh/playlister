import urllib
import urllib2
from bs4 import BeautifulSoup

search_url = "https://www.youtube.com/results?search_query="

def query_video_url(search):
    query = urllib.quote(search)
    response = urllib2.urlopen(search_url + query)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        if vid['href'][1:6] == 'watch':
            return 'https://www.youtube.com' + vid['href']
