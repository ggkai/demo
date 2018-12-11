#stanfordcorenlp
'''
NE类型支持：位置、人物、组织、货币、百分比、日期、时间
'''
from stanfordcorenlp import StanfordCoreNLP

sentence = '清华大学位于北京。'
with StanfordCoreNLP('/Users/guokai/Downloads/stanford-corenlp-full-2018-02-27', lang='zh') as nlp:
    print(nlp.word_tokenize(sentence))
    print(nlp.pos_tag(sentence))
    print(nlp.ner(sentence))
    print(nlp.parse(sentence))
    print(nlp.dependency_parse(sentence))

#pyltp
'''
NE类型支持：人名、地名、机构名
'''
from pyltp import NamedEntityRecognizer
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load('/Users/guokai/Desktop/ltp_data_v3.4.0/ner.model')  # 加载模型
words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
nertags = recognizer.recognize(words, postags)  # 命名实体识别
print ('\t'.join(netrags))
recognizer.release()  # 释放模型