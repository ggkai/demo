#!/usr/bin/python3
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输出 2 到 100 的质数
prime = []
for num in range(2,100):  # 迭代 2 到 100 之间的数字，不包括100
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环，break跳出不会执行else
   else:                  # 循环的 else 部分
      prime.append(num)
print (prime)