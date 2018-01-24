#!/usr/bin/python
'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''


def maxHouseRobber(nums):
    if nums is None or len(nums)==0:
        return 0
    dp=[0 for i in range(len(nums))]
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dp[i]=max(dp[i-1], nums[i]+dp[i-2])
    
    return dp[-1]

















'''
def maxHouseRobber(nums):
    if nums is None or len(nums) == 0:
        return 0
    dp = [0 for i in range(len(nums))]
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2,len(nums)):
        dp[i]=max(dp[i-1], nums[i]+dp[i-2])
    print dp   
    return dp[-1]
'''
nums = [1,2,3,4]
print maxHouseRobber(nums)