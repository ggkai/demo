import requests
from bs4 import BeautifulSoup

#爬详细页的数据
url='http://bj.xiaozhu.com/fangzi/22317292103.html'
header={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
wb_data=requests.get(url,headers=header)
soup=BeautifulSoup(wb_data.text,'lxml')
title=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
address=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
Daily_rent=soup.select('div.day_l > span')
image1=soup.select('curBigImage')
lorder_image=soup.select('div.js_box.clearfix > div.member_pic > a > img')
lorder_gender=soup.select('span.member_girl_ico')
lorder_name=soup.select('a.lorder_name')
data={
    'title':title.get_text(),
    'image1':image1.get('src'),
    'address':address.get_text(),
    'lorder_image':lorder_image.get('src'),
    'lorder_gender':lorder_gender.get_text(),
    'lorder_name':lorder_name.get_text()
}

print(data)