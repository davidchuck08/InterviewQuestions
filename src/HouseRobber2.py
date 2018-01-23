#!/usr/bin/python

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

nums = [1,2,1,1,5,10]
print HouseRobber2(nums)