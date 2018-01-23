#!/usr/bin/python

def longestCommonSubsequence(strA, strB):
    if strA is None or len(strA) == 0:
        return 0
    if strB is None or len(strB) == 0:
        return 0
    
    dp = [[0 for i in range(len(strA)+1)] for j in range(len(strB)+1)]
    
    for i in range(len(strA)):
        for j in range(len(strB)):
            if i is 0 or j is 0:
                dp[i][j]=0
            elif strA[i] == strB[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print dp
    return dp[-1][-1]
    
strA='fabcd'
strB='dabcd'

print longestCommonSubsequence(strA, strB)