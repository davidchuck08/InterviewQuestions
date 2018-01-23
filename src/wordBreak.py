#!/usr/bin/python

def wordBreak(str, dict):
    if str is None or len(str)== 0:
        return False
    strLen = len(str)
    res = [False for i in range(strLen+1)]
    res[0]=True
    for i in range(1,strLen+1):
        for j in range(i):
            if res[j] and str[j:i] in dict:
                res[i] = True
                
    return res

str='Apple'
dict=['Apple', 'Orange']

print wordBreak(str, dict)