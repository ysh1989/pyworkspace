#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import math
'''
这是一个多行注释
注释的是什么我也不是很清楚
'''
'''
x='a';y='b'
print x
print y

print '------'
print x,
print y
'''
'''flag = False
name = 'luren'
print '\a\b'
'''

total = 0 #这是一个全局变量
Money = 2000

def sum(num1, num2):
    total = num1 + num2
    print "函数内是局部变量 : ", total

#调用sum函数
sum(10, 20)
print "函数外是全局变量 : ", total

def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print Money
AddMoney()
print Money


content = dir(math)

print content;




