from gmail import GMail, Message
from random import choice

gmail = GMail("taken.jb2@gmail.com","02103845367")
#msg = Message('lab1',to='c4e.201708@gmail.com',text='em chao anh a.')

html_template='''<p><span style=color: #ff0000;>Xin nghi om</span></p>
<h1>em chào anh, sáng nay tỉnh dậy em cảm thấy rất {sickness} , có lẽ là vì {reason} nên là hôm nay anh cho em nghỉ làm nhé. Em cảm ơn anh nhiều !!.</h1>
</blockquote>'''

d =['đau bụng','đau đầu','đau chân']


r = ['tối hôm qua em ăn linh tinh','hôm qua em uống hơi nhiều','chiều qua chơi thể thao em bị lật cổ chân']
i = choice(d, r)
html_content= html_template.replace('{sickness}','{reason}',i)

#em ko toi uu hoa dc cai replace dict vao html_template, va cung ko dat dc gio luon. anh huong dan giup em nhe :(

msg = Message('Xin nghi om',to='taken.jb@gmail.com',html=html_content)
gmail.send(msg)
