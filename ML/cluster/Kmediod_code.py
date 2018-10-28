# k-mediod算法
from pandas import DataFrame,Series #导入所需要的两个函数
from numpy import zeros
n = 50    #待聚类样本个数
###一组带索引的数组
x = Series(range(1,n+1))      #样本的x坐标值
y = Series(range(n,n+n))      #样本的y坐标值
center0 = Series([x[0],y[0]]) #初始第一个类中心
center1 = Series([x[1],y[1]]) #初始第二个类中心
dis = DataFrame(index=range(0,n),columns=['dis_cen0','dis_cen1','class']) #初始数据框
#=====自定义求最小值位置的函数=====
def which_min(x):
    if x[0] <= x[1]:
        z=0
    else:
        z=1
    return z
#=====主循环开始=====
while True:
    for i in range(0,n):       #求各样本至各类中心的距离
        dis.ix[i,0] = ((x[i]-center0[0])**2+(y[i]-center0[1])**2)**0.5
        dis.ix[i,1] = ((x[i]-center1[0])**2+(y[i]-center1[1])**2)**0.5
        dis.ix[i,2] = which_min(dis.ix[i,0:2]) #样本归类
    index0 = dis.ix[:,2] == 0  #第一类样本序号
    index1 = dis.ix[:,2] == 1  #第二类样本序号
    #====求新类中心===
    x0 = x[index0]
    x0.index = range(sum(index0))
    y0 = y[index0]
    y0.index = range(sum(index0))
    x1 = x[index1]
    x1.index = range(sum(index1))
    y1 = y[index1]
    y1.index = range(sum(index1))
    dis0 = zeros([sum(index0),sum(index0)])
    for i in range(sum(index0)):
        for j in range(sum(index0)):
            dis0[i,j] = ((x0[i]-x0[j])**2+(y0[i]-y0[j])**2)**0.5
    dis1 = zeros([sum(index1),sum(index1)])
    for i in range(sum(index1)):
        for j in range(sum(index1)):
            dis1[i,j] = ((x1[i]-x1[j])**2+(y1[i]-y1[j])**2)**0.5
    center0_new = Series([x0[dis0.sum(axis=1).argmin()],y0[dis0.sum(axis=1).argmin()]])
    center1_new = Series([x1[dis1.sum(axis=1).argmin()],y1[dis1.sum(axis=1).argmin()]])
    #====判定类中心是否发生变化,否则中止while循环====
    if sum(center0==center0_new)+sum(center1==center1_new)==4:
        break
    #====更新类中心
    center0 = center0_new
    center1 = center1_new
print(dis) #输出结果
print(center0)
print(center1)
