#!/usr/bin/python
'''
After robbing those houses on that street, 
the thief has found himself a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
def robberHelper(nums, start, end):
    if start >= len(nums) or end >= len(nums):
        return 0
    dp=[0 for i in range(len(nums))]
    dp[start]=nums[start]
    dp[start+1] = max(nums[start], nums[start+1])
    for i in range(start, end+1):
        dp[i]=max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

def HouseRobber2(nums):
    if nums is None or len(nums)==0:
        return 0
    max1=robberHelper(nums, 0, len(nums)-2)
    max2=robberHelper(nums,1,len(nums)-1)
    
    return max(max1,max2)























'''
def houserHelper(nums, start, end):
    if start >= len(nums) or end >= len(nums):
        return 0
    if start == end:
        return nums[start]
    dp = [0 for i in range(len(nums))]
    dp[start] = nums[start]
    dp[start+1] = max(nums[start], nums[start+1])
    for i in range(2, end+1):
        dp[i] = max(nums[i], dp[i-2]+nums[i])
    return dp[end]

def HouseRobber2(nums):
    if nums is None or len(nums)==0:
        return 0
    max1=houserHelper(nums, 0, len(nums)-2)
    max2 = houserHelper(nums, 1, len(nums)-1)
    return max(max1,max2)
'''
nums = [1,2,1,1,5,10]
print HouseRobber2(nums)