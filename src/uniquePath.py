#!/usr/bin/python

def numUniquePath(nums):
    if nums is None or len(nums) == 0:
        return 0
    row = len(nums[0])
    col = len(nums)
    dp = [[0 for i in range(len(nums[0]))] for j in range(len(nums))]
    print dp
    for i in range(row):
        dp[i][0]=1
    for j in range(col):
        dp[0][j] = 1
    
    for i in range(1,row):
        for j in range(1, col):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print dp
    return dp[-1][-1]

row=3
col=3

nums =[[0 for i in range(row)] for i in range(col)]
print numUniquePath(nums)