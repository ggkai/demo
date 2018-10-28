from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.naive_bayes import GaussianNB,MultinomialNB
transformer = TfidfTransformer()  #转化tf-idf权重向量函数
vectorizer = CountVectorizer()    #转化词频向量函数
# corpus:6篇文档
corpus = [
    'My dog has flea problems, help please.',
    'Maybe not take him to dog park is stupid.',
    'My dalmation is so cute. I love him my.',
    'Stop posting stupid worthless garbage.',
    'Mr licks ate mu steak, what can I do?.',
    'Quit buying worthless dog food stupid'
]
labels = [0,1,0,1,0,1]   #文档标签
word_vec = vectorizer.fit_transform(corpus)  #转成词向量
words = vectorizer.get_feature_names()       #单词集合
word_cout = word_vec.toarray()               #转成ndarray

tfidf = transformer.fit_transform(word_cout) #转成tf-idf权重向量
tfidf_ma = tfidf.toarray()                   #转成ndarray

clf = GaussianNB().fit(tfidf_ma[:4,:],labels[:4])
res = clf.predict(tfidf_ma[4:,:])
print(res)