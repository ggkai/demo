import snownlp

text1='臺灣，这个城市真心很赞'
text2='不好吗，不好意思'
text3='''自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。自然语言处理是一门融语言学、计算机科学、数学于一体的科学
'''
text4=[['这篇','文章'],['那篇','论文'],['好文']]

s=snownlp.SnowNLP(text2)

#分词
print('分词:',s.words)
#词性
for i in s.tags:
    print('词性:',i)
#情感
print('情感:',s.sentiments)
#简体文本转拼音
print('拼音:',s.pinyin)
#繁体转简体
print('简体:',s.han)
#文本转句子
print('句子:',s.sentences)


ss=snownlp.SnowNLP(text3)
#关键词提取
print('关键词:',ss.keywords(limit=5,merge=True))
#文本摘要
print('摘要:',ss.summary(limit=2))
#字频
print('字频:',ss.tf)
#逆文档概率
print('概率:',ss.idf)


sss=snownlp.SnowNLP(text4)
#文本相似度
print('相似度',sss.sim([u'文章']))

