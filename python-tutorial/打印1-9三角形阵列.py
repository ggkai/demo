#!/usr/bin/python3

s = 'qazxswedcvfr'
for i in range(0,len(s),2):
    print (s[i])
for (index,char) in enumerate(s):
    print ("index=%s ,char=%s" % (index,char))