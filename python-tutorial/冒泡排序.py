#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 冒泡排序# 定义列表 list
arays = [1,8,2,6,3,9,4]
for i in range(len(arays)):
    for j in range(i):
        print('i=',i,'j=',j)
        if arays[i] < arays[j]:
            # 实现连个变量的互换
            print(arays[i], arays[j])
            arays[i], arays[j] = arays[j], arays[i]
            print(arays)

print('-------分割线-------')

sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print (i,j)