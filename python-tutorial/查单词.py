#coding:utf-8

# 字典创建  while开关 字典添加   字典寻找
dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c' :
    flag = input("添加或查找单词 ?(a/c)")
    if flag == "a" :                             # 开启
        word = input("输入单词(key):")
        defintion = input("输入定义值(value):")
        dictionary[str(word)] = str(defintion)  # 添加字典
        print ("添加成功!")
        pape = input("您是否要查找字典?(a/0)")   #read
        if pape == 'a':
            print (dictionary)
        else :
            continue
    elif flag == 'c':
        check_word = input("要查找的单词:")  # 检索
        for key in sorted(dictionary.keys()):            # yes
            if str(check_word) == key:
                print ("该单词存在! " ,key, dictionary[key])
                break
            else:                                       # no
                off = 'b'
        if off == 'b':
            print ("抱歉，该值不存在！")
    else:                               # 停止
        print ("error type")
        break