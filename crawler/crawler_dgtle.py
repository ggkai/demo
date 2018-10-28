from bs4 import BeautifulSoup
import requests
import re
'''
问题：爬不到数据
'''
url='http://www.dgtle.com/portal.php'
wb_data=requests.get(url)
soup=BeautifulSoup(wb_data.text,'lxml')
images=soup.select('li.list-group-item.img-box > a.mix_img')
titles=soup.select('li.list-group-item.cards-content > h3 > a')

for image,title in zip(images,titles):
    data={
        'image':image.get('style'),
        'title':title.get_text()
    }
    print(data)

#background-image:url(http://s2.dgtle.com/portal/201801/25/100633vsp82hd8ggi577g6.jpg?imageView2/2/w/960/q/100)
#image=re.search('[background-image:url(]\b[)]\B',image.get('style'))