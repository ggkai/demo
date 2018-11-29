'''
https://matplotlib.org/gallery/index.html
https://matplotlib.org/tutorials/index.html
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

#曲线图
plt.figure(1)
a=[1,2,3,4]
plt.plot(a)

plt.figure(2)
plt.plot([1,2,3,4],[1,4,9,16])

plt.figure(3)
plt.plot([1,2,3,4],[1,4,9,16],'ro')

plt.figure(4)
b=np.arange(0,5,0.2)
plt.plot(b,b,'r--',b,b**2,'bs',b,b**3,'g^')

#直方图
plt.figure(5)
c=100+15*np.random.randn(1000)
plt.hist(x=c,bins=50,density=1,color='g',alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('histogram')
plt.text(x=60,y=0.025,s=r'$\mu=100,\sigma=15$')
plt.axis(xmin=40,xmax=160,ymin=0,ymax=0.04)
plt.annotate(s='hello',xy=(120,0.01),xytext=(140,0.02),arrowprops = dict(color='k',arrowstyle='->'))
plt.grid(True)

#柱状图
plt.figure(6)
d=np.arange(10)
e=np.random.uniform(0,10,10)
f=np.random.uniform(0,10,10)
plt.bar(x=d,height=e,width=0.3,edgecolor='w')
plt.bar(x=d+0.3,height=f,width=0.3,edgecolor='w')

plt.figure(7)
d=np.arange(10)
e=np.random.uniform(0,10,10)
f=np.random.uniform(0,10,10)
plt.bar(x=d,height=e,width=0.5,edgecolor='w',facecolor='#9999ff')
plt.bar(x=d,height=-f,width=0.5,edgecolor='w',facecolor='#ff9999')
for x, y in zip(d,e):
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(d,f):
    plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')

#散点图
plt.figure(8)
e=np.random.randn(1,100)
f=np.random.randn(1,100)
g=np.arctan2(e,f)
plt.scatter(x=e,y=f,s=25,c=g,alpha=0.4,marker='o')#c是散点的颜色，s是散点的大小

#饼状图
plt.figure(9)
h=[u'part1',u'part2',u'part3']
i=[60,30,10]
j=['r','y','b']
plt.pie(x=i,labels=h)

#箱线图
plt.figure(10)
k=pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','e'])
plt.boxplot(x=k)

#3D散点图
fig=plt.figure(11)
ax=Axes3D(fig)
l=np.random.normal(0,1,100)
m=np.random.normal(0,1,100)
n=np.random.normal(0,1,100)
ax.scatter(xs=l, ys=m, zs=n)

#3D线型图
fig=plt.figure(12)
ax=Axes3D(fig)
o=np.linspace(-6*np.pi,6*np.pi,100)
p=np.sin(o)
q=np.cos(o)
ax.plot(xs=o,ys=p,zs=q)

#3D柱状图
fig=plt.figure(13)
ax=Axes3D(fig)
x = [0, 1, 2, 3, 4, 5, 6]
for i in x:
  y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  z = abs(np.random.normal(1, 10, 10))
  ax.bar(left=y, height=z,zs=i, zdir='y', color=['r', 'g', 'b', 'y'])

#3D曲面图
fig=plt.figure(14)
ax=Axes3D(fig)
x=np.arange(-2,2,0.1)
y=np.arange(-2,2,0.1)
x,y=np.meshgrid(x,y)
z=np.sqrt(x**2+y**2)
ax.plot_surface(X=x,Y=y,Z=z,cmap=plt.cm.winter)

#3D线型散点混合图
fig=plt.figure(15)
ax=Axes3D(fig)
x1=np.linspace(-3*np.pi,3*np.pi,500)
y1=np.sin(x1)
z1=np.cos(x1)
ax.plot(xs=x1,ys=y1,zs=z1)

x2=np.random.normal(0,1,100)
y2=np.random.normal(0,1,100)
z2=np.random.normal(0,1,100)
ax.scatter(xs=x2,ys=y2,zs=z2)

#等高线
plt.figure(16)
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
x,y=np.meshgrid(x,y)
contourf(x,y,f(x,y),8,alpha=0.75,cmap='jet')


#图片



plt.show()

'''
补充：绘图设置
坐标轴
标题
图例
数据标签
趋势线
误差线
设置图形svg、png
中文显示
'''
