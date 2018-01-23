#!/usr/bin/python
import math, sys
def perfectSequare(n):
    maxRoot = math.sqrt(n)
    dp =[sys.maxint for i in range(n+1)]
    dp[0]=0
    for i in range(1,n+1):
        for j in range(1,int(maxRoot)+1):
            if j*j == i:
                dp[i]=1
            elif i >= j*j:
                dp[i]=min(dp[i], dp[i-j*j]+1)
    print dp
    return dp[-1]

n = 4

print perfectSequare(n)