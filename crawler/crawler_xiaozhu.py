from bs4 import BeautifulSoup
import requests
import time

#爬虫几个列表的数据，xiaozhu.com
#判断房东性别
def get_lorder_gender(class_name):
    if class_name==['member_girl_ico']:
        return '男'
    else:
        return '女'

#从列表页面获得详细页面链接
def get_links(single_url):
    time.sleep(2)
    wb_data = requests.get(single_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get('href')
        get_detail_info(href)

#从详细页面链接获得详细数据
def get_detail_info(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    images=soup.select('#curBigImage')
    titles=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    prices=soup.select('#pricePart > div.day_l > span')
    avartars=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    loder_names=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    genders=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    for image,title,ads,price,avartar,loder_name,gender in zip(images,titles,address,prices,avartars,loder_names,genders):
        #从标签里面提取内容
        data={
            'image':image.get('src'),
            'title':title.get_text(),
            'address':ads.get_text(),
            'price': price.get_text(),
            'avartar': avartar.get_text(),
            'loder_name': loder_name.get_text(),
            'gender': gender.get_lorder_gender(gender.get('class'))
        }
        print(data)

#获取列表页面地址
urls = ['http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1, 10)]

#获取列表页面
for single_url in urls:
    get_links(single_url)
