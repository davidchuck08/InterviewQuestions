#!/usr/bin/python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
A transaction is a buy & a sell. You may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
'''

def getProfit3(nums):
    if nums is None or len(nums)==0:
        return 0
    before =[0 for i in range(len(nums))]
    beforeMin = nums[0]
    beforeProfit=0
    
    after=[0 for i in range(len(nums))]
    afterMax=nums[-1]
    afterProfit=0
    
    for i in range(len(nums)):
        beforeProfit = max(beforeProfit, nums[i]-beforeMin)
        before[i]=beforeProfit
        beforeMin = min(beforeMin, nums[i])
        
        afterProfit = max(afterProfit, afterMax-nums[len(nums)-i-1])
        after[len(nums)-i-1]=afterProfit
        afterMax = max(afterMax,nums[len(nums)-i-1])
        
    res=0
    for i in range(len(nums)):
        res = max(res, before[i]+after[i])
    print before
    print after
    return res
'''  
def getProfit3(nums):
    if nums is None or len(nums) == 0:
        return 0
    before =[0 for i in range(len(nums))]
    beforeMin=nums[0]
    beforeMax=0
    after = [0 for i in range(len(nums))]
    afterMax=nums[-1]
    afterProfit=0
    for i in range(len(nums)):
        
        if beforeMax < nums[i]-beforeMin:
            beforeMax=nums[i]-beforeMin
        before[i]=beforeMax
        beforeMin=min(nums[i], beforeMin)
        
        if afterProfit < afterMax - nums[len(nums)-1-i]:
            afterProfit = afterMax - nums[len(nums)-1-i]
        after[len(nums)-1-i]=afterProfit
        afterMax=max(nums[len(nums)-1-i],afterProfit)
    maxProfit=0
    for i in range(len(nums)):
        if maxProfit < before[i]+after[i]:
            maxProfit = before[i]+after[i]
    print before
    print after        
    return maxProfit
'''
nums=[1,4,5,7,6,3,2,9]
print getProfit3(nums)