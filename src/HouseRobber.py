#!/usr/bin/python

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
        dp[i]=max(nums[i], nums[i]+dp[i-2])
    print dp   
    return dp[-1]

nums = [1,2,3,4]
print maxHouseRobber(nums)