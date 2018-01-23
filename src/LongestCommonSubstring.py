#!/usr/bin/python

def getLongestCommonSubstring(strA, strB):
    if strA is None or len(strA) is None:
        return 0
    if strB is None or len(strB) is None:
        return 0
    
    dp =[[0 for i in range(len(strA))] for j in range(len(strB))]
    maxLen =0
    for i in range(len(strA)):
        for j in range(len(strB)):
            if strA[i] == strB[j]:
                if i is 0 or j is 0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+1
                if maxLen < dp[i][j]:
                    maxLen = dp[i][j] 
    print dp   
    return maxLen

strA = 'abcd'
strB= 'abce'

print getLongestCommonSubstring(strA, strB)