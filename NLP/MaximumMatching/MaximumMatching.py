import re
#读入词典
with open('MaximumMatchingDict.txt','r') as f:
    dic=f.read()
#去掉空格,替换为空
dic=re.sub(' ','',dic)

#待分词对象
s1='今天我们要学习电商产品评价数据情感分析案例'

#存储分词
s2=str()

#最大词长度
maxlen=5

#初始取词
w=s1[:5]

#判断内容，s1中没有内容就终止
while len(s1)>0:
    if w in dic:
        s2=s2+'/'+w
        s1=s1[len(w):]
        w=s1[:maxlen]
    elif len(w)==1:
        s2 = s2+'/'+w
        s1 = s1[len(w):]
        w = s1[:maxlen]
    else:
        w = w[:len(w)-1]
print(s2)