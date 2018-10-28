#!/usr/bin/python
#coding=UTF-8

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j," ",'\t',end='')
    print(end='\n')
#加边框
for i in range(1,10):
    li=[];
    for j in range(1,i+1):
        li.append('%s x %s = %s'%(j,i,i*j))
    print(li);