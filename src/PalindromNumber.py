#!/usr/bin/python

def palindromeNumber(num):
    if num < 0:
        return False
    
    divider=1
    localNum = num
    while localNum > 10:
        divider *=10
        localNum = localNum/10
    localNum = num
    while localNum != 0:
        left = localNum / divider
        right = localNum % 10
        if left != right:
            return False
        localNum = localNum % divider
        localNum  = localNum / 10
        divider = divider/100
    return True

num=1213

print palindromeNumber(num)