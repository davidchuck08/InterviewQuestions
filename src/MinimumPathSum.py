#!/usr/bin/python

def minimumPathSum(nums):
    if nums is None or len(nums) == 0:
        return 0
    
    row = len(nums[0])
    col = len(nums)
    dp =[[0 for i in range(len(nums[0]))] for j in range(len(nums)) ]
    
    for i in range(1,row):
        dp[i][0]=dp[i-1][0]+nums[i][0]
    for j in range(1,col):
        dp[0][j]=dp[0][j-1]+nums[0][j]
    for i in range(1,row):
        for j in range(1, col):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i][j-1]+nums[i][j]
            else:
                dp[i][j]=dp[i-1][j]+nums[i][j]
    
    return dp[-1][-1]

c1=[1,2]
c2=[1,1]

nums=[]
nums.append(c1)
nums.append(c2)

print minimumPathSum(nums)