url = 'https://www.apple.com/itunes/charts/songs/'
output_file_name = 'new.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup

#1.download trang web
conn = urlopen('https://www.apple.com/itunes/charts/songs/')
data = conn.read()
html_content = data.decode('utf-8')
# print(html_content)

html_file = open('apple.html','wb')
html_file.write(data)
html_file.close()
#2.tim vung quan tam
#3.lay thong tin quan tam

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section','section chart-grid')
div = section.find('div', 'section-content')
ul = div.find('ul')
li_list = ul.find_all('li')
# print(li_list)

# for li in li_list:
#     print(li.prettify())
#     print('*'* 50)
# li = li_list[0]

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

import pyexcel
pyexcel.save_as(records=new_list, dest_file_name='Ex1.xlsx')
