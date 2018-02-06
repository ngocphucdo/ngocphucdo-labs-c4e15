url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
output_file_name = 'new.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup

conn = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
data = conn.read()
html_content = data.decode('utf8')
print(html_content)

html_file = open('cafef.html','wb')
html_file.write(data)
html_file.close()

soup = BeautifulSoup(html_content, 'html.parser')
div_align = soup.find('center','divTop')
div_cf_RedCBox = div_align.find('cf_RedCBox','width: 840px;overflow:hidden;border-bottom:solid 1px #cecece','cf_ContainerBox')
div_cf_BoxContent1 = div_cf_RedCBox.find('cf_BoxContent')
div_cf_RedireBox = div_cf_BoxContent1.find('cf_RedireBox')
div_cf_BoxContent2 = div_cf_RedireBox.find('cf_BoxContent')
div_cf_researchData = div_cf_BoxContent2.find('cf_ResearchDataHistoryInfo')
div_style = div_cf_researchData.find('width: 100%; float: left; padding-left: 0px; background-color: #E1E1E1;','left')
div_tab_header = div_style.find('divTableHeader')
tr_list = div_tab_header.find_all('tr')
print(tr_list)
