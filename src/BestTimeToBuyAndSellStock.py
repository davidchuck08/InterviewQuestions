#!/usr/bin/python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

'''

def maxProfit(nums):
    if nums is None or len(nums)==0:
        return 0
    maxProfit=0
    minPrice=nums[0]
    for i in range(len(nums)):
        maxProfit=max(maxProfit, nums[i]-minPrice)
        minPrice=min(minPrice,nums[i])
    return maxProfit
def maxProfile(nums):
    if nums is None or len(nums) == 0:
        return 0
    minPrice=nums[0]
    maxProfit = 0
    for i in range(len(nums)):
        maxProfit = max(maxProfit, nums[i]-minPrice)
        minPrice = min(nums[i],minPrice)
        
    return maxProfit

nums=[10,20,30,4,50,70]
print maxProfit(nums)