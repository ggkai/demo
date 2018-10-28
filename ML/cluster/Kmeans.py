#用sklearn中k-means算法对鸢尾花进行聚类
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn import datasets

#下载鸢尾花数据集
iris = datasets.load_iris()

x = iris.data#获取数据
y = iris.target#获取真实分类

#创建KMeans模型，设置聚类参数
kModel = KMeans(n_clusters=3)

#训练模型
kModel.fit(x)

#模型类中心
kModel.cluster_centers_

#聚类
kModel.labels_

#对比真实值和训练值
a={'True':[i for i in y],
   'Pred':[j for j in kModel.labels_]}

dat = DataFrame(a)

print(dat)

