#!/usr/bin/python
'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
def factoringTrailingZero(num):
    if num == 0:
        return 0
    else:
        return num/5+factoringTrailingZero(num/5)


'''

def factoringTrailingZero(num):
    if num == 0:
        return 0
    else:
        return num/5+factoringTrailingZero(num/5)
''' 
num = 6
print factoringTrailingZero(num)