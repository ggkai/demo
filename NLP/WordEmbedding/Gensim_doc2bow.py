import jieba
from gensim import corpora, models, similarities

documents = [
    '0无偿居间介绍买卖毒品的行为应如何定性',
    '1吸毒男动态持有大量毒品的行为该如何认定',
    '2如何区分是非法种植毒品原植物罪还是非法制造毒品罪',
    '3为毒贩贩卖毒品提供帮助构成贩卖毒品罪',
    '4将自己吸食的毒品原价转让给朋友吸食的行为该如何认定',
    '5为获报酬帮人购买毒品的行为该如何认定',
    '6毒贩出狱后再次够买毒品途中被抓的行为认定',
    '7虚夸毒品功效劝人吸食毒品的行为该如何认定',
    '8妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
    '9一方未签字办理的结婚登记是否有效',
    '10夫妻双方1990年按农村习俗举办婚礼没有结婚证 一方可否起诉离婚',
    '11结婚前对方父母出资购买的住房写我们二人的名字有效吗',
    '12身份证被别人冒用无法登记结婚怎么办？',
    '13同居后又与他人登记结婚是否构成重婚罪',
    '14未办登记只举办结婚仪式可起诉离婚吗',
    '15同居多年未办理结婚登记，是否可以向法院起诉要求离婚'
]
stopword='的 0 1 2 3 4 5 6 7 8 9 11 12 13 14 15 如何 可以'#停用词字符串
stoplist=set(stopword.split(' '))#停用词集合

'''
gemsim doc2bow
'''
texts=[[word for word in jieba.cut(document,cut_all=True) if word not in stoplist] for document in documents]#分词
dict=corpora.Dictionary(texts)#词典
corpus=[dict.doc2bow(text) for text in texts]#词袋模型
print('doc2bow:',corpus)
print('doc2bow:',dict.token2id)

'''
gensim tfidf
'''
tfidf = models.TfidfModel(corpus)# train the model
corpus_tfidf=tfidf[corpus]# 获得tfidf
for doc in corpus_tfidf:
    print('tfidf:',doc)

'''
gensim new tfidf
'''
text2='16同居多年未办理结婚登记'
text2_bow=dict.doc2bow(jieba.cut(text2))
text2_tfidf=tfidf[text2_bow]
print('tfidf2:',text2_tfidf)

'''
gensim LDA
'''
lda=models.LdaModel(corpus=corpus_tfidf,id2word=dict,num_topics=2)
corpus_lda=lda[corpus_tfidf]
print('lda_topics:',lda.print_topics())
for doc in corpus_lda:
    print('corpus_lda:',doc)

'''
gensim LSI(Latent Semantic Indexing)
'''
lsi=models.LsiModel(corpus=corpus_tfidf,id2word=dict,num_topics=2)
corpus_lsi=lsi[corpus_tfidf]
print('lsi_topics:',lsi.print_topics(2))
for doc in corpus_lsi:
    print('corpus_lsi:',doc)

'''
gensim DP(Random Projections)
'''
rp=models.RpModel(corpus=corpus_tfidf,id2word=dict,num_topics=2)
corpus_rp=rp[corpus_tfidf]
for doc in corpus_rp:
    print('corpus_rp:',doc)

'''
gensim similarity
'''
text3='妻子下落不明丈夫又与他人登记结婚是否为无效婚姻'
simi_bow=dict.doc2bow(jieba.cut(text3))
simi_tfidf=tfidf[simi_bow]
similarity = similarities.Similarity(output_prefix='-Similarity-index', corpus=corpus, num_features=999)#相似性索引
corpus_similarity=similarity[simi_bow]#similarity检索,tfidf或者bow
print('corpus_similarity:',corpus_similarity)
