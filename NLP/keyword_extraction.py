#jieba
import jieba
import jieba.analyse
import jieba.posseg

text="香奈儿的高级手工坊香奈儿CHANEL前天精湛手工艺每年12月，卡尔·拉格斐都会以系列作品，向香奈儿Métiersd'Art高级手工坊致敬。这些手工坊对传统与现代技艺加以不断创新，将不可能变为可能，解决了各种工艺上的复杂性。金银饰坊创立于 1950Goossens金银饰坊与香奈儿的合作始于1953年，之前工坊的创始人罗伯特·古森（Robert Goossens）与嘉柏丽尔·香奈儿一直有着密切的合作。他的风格与技艺融会贯通了雕塑、金器打造与服饰珠宝设计，自成一派。他打造的系列作品造型轻盈，为香奈儿提供了无尽的灵感。鞋履坊创立于 1894自1957年为嘉柏丽尔·香奈儿定制双色鞋以来，Massaro鞋履坊与香奈儿的合作从未停歇。2002年，Massaro鞋履坊正式加入香奈儿Métiers d'Art高级手工坊。每一季，Massaro鞋履坊都以无与伦比的精湛工艺回应卡尔·拉格斐的卓绝创意，打造出别具一格、气质优雅的精工鞋履。刺绣坊创立于 18581983年，卡尔·拉格斐加入香奈儿，由此开启与Lesage刺绣坊的合作。每一季，Lesage刺绣坊都将设计师的创意化为精美作品。秉承珍罕独特的高超工艺，Lesage刺绣坊的灵巧绣匠在服装与配饰上营造出各种华美刺绣。1990年代，出于开拓新业务的需要，Lesage刺绣坊设立了纺织工坊，以纷繁多样的织线打造出匠心独运、精美绝伦的Lesage刺绣斜纹软呢。服饰珠宝坊创立于1929巧妙结合精湛手工艺与创意巧思，是“饰品名匠”Desrues服饰珠宝坊的专长。Desrues服饰珠宝坊由GeorgesDesrues创立于1929年，每一季都为香奈儿定制钮扣、珠宝、腰带扣及手袋转扣等精美作品。Desrues服饰珠宝坊自1965年起与香奈儿合作，于1985年成为首个加入香奈儿Métiersd'Art高级手工坊的成员。山茶花及羽饰坊创立于 1880Lemarié山茶花及羽饰坊由Palmyre Coyette创立，其历史可追溯至1880年。它不仅专攻羽毛与花饰，还擅长制作“服装”（镶饰、荷叶边、褶绣…）以及各种褶饰。1996年加入香奈儿Métiersd'Art高级手工坊的Lemarié山茶花及羽饰坊，在卡尔·拉格斐每年设计的十个香奈儿系列中占据举足轻重的核心地位。褶饰坊创立于1853Lognon褶饰坊结合传统工艺与数字科技，展现前所未有的非凡技艺。工匠在平坦的面料上灵巧地捏出丰盈的褶裥，如此高超的技艺意味着对动作精度的极高要求和对各种材质特点的细致把握。完美的褶饰，需要两位褶饰工匠心照不宣的默契和协调一致的手法才能得以完成。刺绣坊创立于 1939Montex刺绣坊是一家设立于巴黎的现代刺绣工坊，每一季都以极致摩登的独特图案、精致华美的新颖设计，为香奈儿的系列作品画上点睛之笔。Montex刺绣坊运用结合钩针与绣针的“Lunéville”隐藏式刺绣工艺，以及距今已有上百年历史的手导控式Cornely缝纫机，将这些精美刺绣化为实物。"

text2='无与伦比的精湛工艺回应卡尔·拉格斐的卓绝创意'
text3='向香奈儿Métiersd\'Art高级手工坊致敬'
'''
方法一：TFIDF提取关键词
'''
idf_path='/idf.txt.big'
stop_words_psth='/stopword.txt'
userdict_path='userdict.txt'
pos=('custom','ns','n','vn','nr')

#自定义idf文本语料库路径
# jieba.analyse.set_idf_path(idf_path)
# jieba.analyse.TFIDF(idf_path=pass)

#自定义停用词文本语料库路径
# jieba.analyse.set_stop_words(stop_words_psth)

#动态修改词典
jieba.suggest_freq(('卡尔·拉格','Métiersd\'Art'),True)
jieba.add_word('卡尔·拉格',freq=100,tag='custom')
jieba.add_word('Métiersd\'Art',freq=100,tag='custom')

#自定义词典路径
jieba.load_userdict(userdict_path)

#关键词提取
'''
allowPOS提取的词性类型
a:形容词
d:副词
i:成语
m:数词
n:名词
nr:人名
ns:地名
nt:机构团体
nz:其他专有名词
t:时间
v:动词
x:标点符号
f:方位词
un:未知
'''
tags=jieba.analyse.extract_tags(sentence=text3,topK=10,withWeight=False,allowPOS=())

print(tags)


'''
方法二：TextRank提取关键词
'''
# jieba.analyse.textrank(sentence=text, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
# jieba.analyse.TextRank()

