#!/usr/bin/python

def jumpGame2(nums):
    reach = 0
    lastreach=0
    reachable = True
    steps=0
    if nums is None:
        return 0
    for i in range(len(nums)):
        if i > lastreach:
            steps+=1
            lastreach = reach
        if i > reach:
            reachable =False
            break
        if i+nums[i] > reach:
            reach = i+nums[i]
            
        
    return steps, reachable

nums = [2,2,0,1,4]
num2 = [3,2,1,0,4]
print jumpGame2(nums)
print jumpGame2(num2)  