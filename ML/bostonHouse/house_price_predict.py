#波士顿房价预测
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#获取数据
boston=load_boston()

#输入为RM:住宅平均房间数
x=boston.data
#转换数据格式，作为数组输入
#x1=[[float(str(i))] for i in x]
y=boston.target

lr2=LinearRegression()
lr2.fit(x,y)#拟合模型
print('确定性系数:',lr2.score(x,y))#确定性系数
print('系数:',lr2.coef_)#系数
print('截距:',lr2.intercept_)#截距
print('预测值:',lr2._decision_function(2))#预测值