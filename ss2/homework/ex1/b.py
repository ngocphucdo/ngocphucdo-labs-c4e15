url = 'https://www.apple.com/itunes/charts/songs/'
output_file_name = 'new.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

conn = urlopen('https://www.apple.com/itunes/charts/songs/')
data = conn.read()
html_content = data.decode('utf-8')

html_file = open('apple.html','wb')
html_file.write(data)
html_file.close()

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section','section chart-grid')
div = section.find('div', 'section-content')
ul = div.find('ul')
li_list = ul.find_all('li')

new_list = []
for li in li_list:
    a = li.h3.a
    title = a.string
    a = li.h4.a
    artist = a.string
    news = {
        'title' : title,
        'artist' : artist
    }
    new_list.append(news)
    print(new_list)

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}

for song in new_list:
    dl = YoutubeDL(options)
    dl.download([song['title']])
