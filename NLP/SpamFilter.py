import jieba
import matplotlib.pyplot as plt
import random as rd
import numpy as np
import re
import os
import pandas as pd
from wordcloud import WordCloud

os.chdir('/Users/kai/Downloads/zm-python/垃圾短信过滤')
data=pd.read_csv('message80W1.csv',sep=',',encoding='utf-8',header=None)
data.columns=['id','识别','短信内容']

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
labels ='非垃圾短信','垃圾短信'
plt.axes(aspect=1)
fracs=[data['识别'].value_counts()[0],data['识别'].value_counts()[1]]
explode=[0,0.1]
plt.pie(x=fracs,labels=labels,explode=explode,autopct='%1.1f',shadow=True,labeldistance=1,startangle=90,
        pctdistance=0.6,radius=1)
plt.title('分布情况')
plt.show()

sample_data=data.sample(n=int(len(data)/8),frac=None,replace=False,weights=None,random_state=None,axis=0)
sample_data['识别'].value_counts()
sample_data1=sample_data[sample_data['识别']==0]

new_data=sample_data1.sample(n=(20000-sum(sample_data['识别']==1),fracs=None,replace=))

#数据抽样

#去重

#数据脱敏

#去停用词

#词频统计

#绘制词云
