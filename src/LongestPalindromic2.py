#!/usr/bin/python

def longestPalindromic(str):
    if str is None or len(str) == 0:
        return None
    res = ""
    for i in range(len(str)):
        temp = helper(str, i,i)
        if len(temp) > len(res):
            res = temp
        temp = helper(str, i,i+1)
        if len(temp) > len(res):
            res=temp
            
    return res

def helper(str, l, r):
    if str is None or len(str) == 0:
        return None
    
    while l >=0 and r < len(str) and str[l]==str[r]:
        l-=1
        r+=1
    return str[l+1:r]


str = 'aabcbaa'
print longestPalindromic(str)