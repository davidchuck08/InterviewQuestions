#!/usr/bin/python

def singleNumber(nums):
    x =0
    for num in nums:
        x=x ^ num
        
    return x

nums = [1,1,2,2,3,3,4,5,5]
print singleNumber(nums)