#!/usr/bin/python

def reverseInteger(num):
    negative = False
    if num < 0:
        negative = True
    num = abs(num)
    res = 0
    localNum = num
    while localNum >0:
        mod = localNum %10
        localNum = localNum/10
        
        res = 10*res+mod
        
    if negative == True:
        res = -1*res
        
    return res

num = -0
print reverseInteger(num)