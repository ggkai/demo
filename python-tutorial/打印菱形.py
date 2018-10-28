#!/usr/bin/python
# -*- coding: UTF-8 -*-

#菱形 |x - w/2| + |y - w/2| = w/2
width = int(input('输入对角线长度： '))
for row in range(width + 1):
    for col in range(width + 1):
        if ((abs(row - width/2) + abs(col - width/2)) == width/2):
            print ("*")
        else:
            print (" ")
    print (" ")

#打印其他形状 http://www.runoob.com/w3cnote/prints-diamonds-triangles-rectangles.html