#!/usr/bin/python
'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is 
formed from the original string by deleting some (can be none) of the characters without 
disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

'''

def distinctSubsequenceTotal(word1, word2):
    m=len(word1)+1
    n=len(word2)+1
    dp=[[0 for j in range(n)] for i in range(m)]
   
    for i in range(m):
        dp[i][0]=1
        
    for i in range(1,m):
        for j in range(1,n):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
       














'''
def distinctSubsequenceTotal(word1, word2):
    m=len(word1)+1
    n=len(word2)+1
    dp=[[0 for i in range(n)] for j in range(m)]
    
    for i in range(m):
        dp[i][0]=1
    for i in range(1,m):
        for j in range(1,n):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m-1][n-1]
'''
word1='rabbbit'
word2='rabbit'
print distinctSubsequenceTotal(word1, word2)