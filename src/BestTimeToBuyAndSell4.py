#!/usr/bin/python
'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''

def getProfit4(nums,k):
    if nums is None or len(nums)==0:
        return 0
    if len(nums)==2:
        return nums[1]-nums[0]
    
    localProfit=[[0 for i in range(len(nums)+1)] for i in range(len(nums))]
    globalProfit=[[0 for i in range(len(nums)+1)] for i in range(len(nums))]
    
    for i in range(1,len(nums)):
        diff = nums[i]-nums[i-1]
        for j in range(1, len(nums)+1):
            localProfit[i][j]=max(globalProfit[i-1][j-1]+max(0, diff), localProfit[i-1][j]+diff)
            globalProfit[i][j]=max(localProfit[i][j], globalProfit[i-1][j])
            
    return globalProfit[len(nums)-1][k]
'''
def getProfit4(nums, k):
    if nums is None or len(nums)==0 or k<1:
        return 0
    if len(nums) == 2:
        return nums[1] - nums[0]
    
    localProfit=[[0 for i in range(len(nums)+1)] for i in range(len(nums))]
    globalProfit=[[0 for i in range(len(nums)+1)] for i in range(len(nums))]
    
    for i in range(1,len(nums)):
        diff = nums[i]-nums[i-1]
        for j in range(1, len(nums)+1):
            
            localProfit[i][j] = max(globalProfit[i-1][j-1]+max(0, diff), localProfit[i-1][j]+diff)
            globalProfit[i][j] = max(localProfit[i][j], globalProfit[i-1][j])
        
    return globalProfit[len(nums)-1][k]
'''

nums = [4,4,6,1,1,4,2,5]
k=2
print getProfit4(nums, k)
