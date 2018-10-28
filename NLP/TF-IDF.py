#文本分类
import re
import numpy as np
import math
from sklearn.naive_bayes import GaussianNB
corpus = [
    'My dog has flea problems, help please.',
    'Maybe not take him to dog park is stupid.',
    'My dalmation is so cute. I love him my.',
    'Stop posting stupid worthless garbage.',
    'Mr licks ate mu steak, what can I do?.',
    'Quit buying worthless dog food stupid'
]
labels = [0,1,0,1,0,1]

#去掉标点符号
data_text=[re.sub('[?,.]','',text).lower() for text in corpus]
data_text=[text.split() for text in data_text]
word_list=[]
[word_list.extend(text) for text in data_text]#转成一个数组
words=tuple(set(word_list))#转成元组

#求TF
n,m=len(data_text),len(words)
tf=np.zeros([n,m])
for i in range(n):
    for j in range(m):
        tf[i,j]=data_text[i].count(words[j])/len(data_text[i])

#求IDF
idf=[]
for i in range(m):
    num=sum([words[i] in data_text[j] for j in range(0,n)])
    idf.append(math.log(n/num))

for i in range(m):
    tf[:,i]=tf[:,i]*idf[i]

#朴素贝叶斯模型
clf = GaussianNB().fit(tf[:4,:],labels[:4])
res = clf.predict(tf[4:,])
print(res)