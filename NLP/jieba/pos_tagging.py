import jieba
import jieba.posseg

text='无与伦比的精湛工艺回应卡尔·拉格斐的卓绝创意'
words=jieba.posseg.cut(sentence=text,HMM=True)
for word,flag in words:
    print('%s %s'%(word,flag))