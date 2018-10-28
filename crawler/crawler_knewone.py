from bs4 import BeautifulSoup
import requests
import time
#爬动态数据

'''
在Network > XHR > headers中可以查看Request URL的页面，根据页码的不同爬取异步加载的数据
'''
#网页
url='https://knewone.com/discover?page='

#构造抓取函数
def get_page(url,data=None):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    images=soup.select('a.cover-inner > img')
    titles=soup.select('section > h4 > a')
    links=soup.select('section > h4 > a')
    if data==None:
        for image,title,link in zip(images,titles,links):
            data={
                'image':image.get('src'),
                'title':title.get_text('title'),
                'link':link.get('href')
            }
            print(data)
#控制爬取页码
def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)

get_more_pages(1,10)