#!/usr/bin/python

def productArray(nums):
    if nums is None or len(nums) == 0:
        return 
    left = [1 for i in range(len(nums))]
    right = [1 for i in range(len(nums))]
    for i in range(1,len(nums)):
        left[i] = left[i-1]*nums[i-1]
    for i in range(len(nums)-1,0,-1):
        right[i-1]=right[i]*nums[i]
    
    res = []
    
    for x in range(len(nums)):
        res.append(left[x]*right[x])
    return res
nums=[1,2,3,4]
print productArray(nums)