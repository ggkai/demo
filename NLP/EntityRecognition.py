#stanfordcorenlp
from stanfordcorenlp import StanfordCoreNLP

sentence = '清华大学位于北京。'

with StanfordCoreNLP(r'G:\JavaLibraries\stanford-corenlp-full-2018-02-27', lang='zh') as nlp:
    print(nlp.word_tokenize(sentence))
    print(nlp.pos_tag(sentence))
    print(nlp.ner(sentence))
    print(nlp.parse(sentence))
    print(nlp.dependency_parse(sentence))

#


#pyltp
import os
LTP_DATA_DIR = '/path/to/your/ltp_data'  # ltp模型目录的路径
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

from pyltp import NamedEntityRecognizer
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
netags = recognizer.recognize(words, postags)  # 命名实体识别

print ('\t'.join(netags))
recognizer.release()  # 释放模型

