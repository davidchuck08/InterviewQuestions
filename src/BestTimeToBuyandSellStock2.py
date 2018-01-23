#!/usr/bin/python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
def maxProfit2(nums):
    if nums is None or len(nums)==0:
        return 0
    profit= 0
    for i in range(1,len(nums)):
        diff = nums[i]-nums[i-1]
        if diff > 0:
            profit+=diff
    return profit
'''     
def maxProfit2(nums):
    if nums is None or len(nums) == 0:
        return 0
    profit=0
    for i in range(1,len(nums)):
        diff = nums[i]-nums[i-1]
        if diff > 0:
            profit+=diff
            
    return profit
'''
nums=[5,1,2,3,4]

print maxProfit2(nums)