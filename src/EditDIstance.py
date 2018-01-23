#!/usr/bin/python
'''
In computer science, edit distance is a way of quantifying how dissimilar two strings (e.g., words) 
are to one another by counting the minimum number of operations required to transform one string into the other.

There are three operations permitted on a word: replace, delete, insert. 
For example, the edit distance between "a" and "b" is 1, the edit distance between "abc" and "def" is 3. 
This post analyzes how to calculate edit distance by using dynamic programming.

'''
def editDistance(word1, word2):
    m=len(word1)
    n=len(word2)
    dp=[[0 for j in range(n)] for i in range(m)]
    
    for i in range(m):
        dp[i][0]=i

    for j in range(n):
        dp[0][j]=j
    for i in range(1,m):
        for j in range(1,n):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
                
    return dp[-1][-1]














'''
def editDistance(word1, word2):
    m=len(word1)+1
    n=len(word2)+1
    dp=[[0 for i in range(n)] for j in range(m)] 
    
    for i in range(m):
        dp[i][0]=i
    for i in range(n):
        dp[0][i]=i
        
    for i in range(1,m):
        for j in range(1,n):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
                
    return dp[m-1][n-1]
'''
word1='abcd'
word2='abcdef'

print editDistance(word1, word2)