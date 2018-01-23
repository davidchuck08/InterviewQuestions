#!/usr/bin/python

def isUglyNumber(num):
    if num == 0: 
        return False
    if num == 1:
        return True
    if (num %2 ==0):
        num=num/2
        return isUglyNumber(num)
    if (num %3 ==0):
        num=num/3
        return isUglyNumber(num)
    if (num %5 ==0):
        num=num/5
        return isUglyNumber(num)
    return False

num = 210
print isUglyNumber(num)