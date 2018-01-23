#!/usr/bin/python
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
'''
def numDecodeWays(str):
    if str is None or len(str) ==0:
        return 0
    
    if len(str) == 1:
        return 1
    dp=[0 for i in range(len(str))]
    dp[0]=1
    
    if str[:2] >'26':
        if str[1:2]!='0':
            dp[1]=1
        else:
            dp[1]=0
    else:
        if str[1:2]!=0:
            dp[1]=2
        else:
            dp[1]=1
            
    for i in range(2,len(str)):
        if dp[i] != '0':
            dp[i]+=dp[i-1]
        temp = int(str[i-1:i+1])
        if temp >=10 and temp <=26:
            dp[i]+=dp[i-2]
    return dp[-1]














'''
def numDecodeWays(str):
    if str is None or len(str) == 0 :
        return 0
    if len(str) == 1:
        return 1
    dp=[0 for i in range(len(str))]
    dp[0]=1
    if int(str[:2]) > 26:
        if str[1:2] != '0':
            dp[1]=1
        else:
            dp[1]=0
    else:
        if str[1:2] !='0':
            dp[1]=2
        else:
            dp[1]=1
            
    for i in range(2, len(str)):
        if str[i] !='0':
            dp[i]+=dp[i-1]
        temp = int(str[i-1:i+1])
        if temp >= 10 or temp <= 26:
            dp[i]+=dp[i-2]
        
    return dp[-1]
'''
str = '125'
print numDecodeWays(str)