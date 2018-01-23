#!/usr/bin/python

def jumpGame(nums):
    if nums is None:
        return True
    if len(nums) <= 1:
        return True
    max = 0
    for i in range(len(nums)):
        if max < i:
            return False
        if i + nums[i] >= max:
            max = i + nums[i]
        if max >= len(nums)-1:
            return True
        
    return False

nums = [2,3,1,1,4]
num2 = [3,2,1,0,4]
print jumpGame(nums)
print jumpGame(num2)        