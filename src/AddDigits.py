#!/usr/bin/python
'''
Math
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
'''
def addDigits(nums):
    numStr=str(nums)
    res=0
    for digit in numStr:
        res+=int(digit)
    if res <10:
        return res
    else:
        return addDigits(res)

'''
def addDigits(nums):
    numStr=str(nums)
    res=0
    for x in numStr:
        res+=int(x)
    if res<10:
        return res
    else:
        res=addDigits(res)
    return res  
'''  
nums=12345
print addDigits(nums)