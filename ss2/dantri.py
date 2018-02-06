url = 'http://dantri.com.vn'
output_file_name = 'new.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup

#1 download trang web
#1.1 mo ket noi voi trang web
# conn = urlopen(url)
#1.2 read
# data = conn.read()  #dang bytes
# #1.3 decode
# html_content = data.decode('utf-8')
# print(html_content)

#Buoc gop ca 3 buoc vao:

data = urlopen(url).read()
html_content = data.decode('utf-8')
# print(html_content)
#day web minh vua down ve vao 1 file

html_file = open("dantri.html","wb") #w = write
html_file.write(data)
html_file.close()

#2 trich vung quan tam

#3 trich thong tin can thiet

#tao ra 1 con soup
soup = BeautifulSoup(html_content, 'html.parser') #dinh dang khac la xml
ul = soup.find('ul', 'ul1 ulnew') #class id    #tra ve 1 soup
li_list = ul.find_all('li')                    #tra ve 1 list cac soup

# for li in li_list:
#     print(li.prettify())
#     print('*' * 20)

#vao dc ul roi toi li roi choc vao h4

# li = li_list[0]   #choc vao vi tri dau tien cua list li
# h4 = li.find('h4')  #=li.h4                      a = li.h4.a cung dc
#
# news_list = []
# for li in li_list:
#     a = h4.a
#     href =url + a['href']
#     title = a.string
#     news = {
#         'title' : title,
#         'link': href
#     }
#     news_list.append(news)
#     print('*'*20)
#
# import pyexcel
# pyexcel.save_as(records=news_list, dest_file_name='NgocPhuc.xlsx')
