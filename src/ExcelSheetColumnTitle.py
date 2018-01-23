#!/usr/bin/python
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet. For example:
     1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

def  columnTitle(num):
    if num is None or num < 1:
        return None
    
    map=dict()
    start=ord('A')
    for i in range(26):
        map[i]=chr(start+i)
    print map
    res=[]   
    while num > 0:
        res.insert(0, chr(num%26+ord('A')))
        num/=26
    print res













'''
def columnTitl(col):
    map=dict()
    start=ord('A')
    for i in range(26):
        map[i+1]=chr(start+i)
    res=[]
    while col >0:
        res.insert(0,map[col%27])
        col /=27
    return "".join(res[:])
'''
col=26
print columnTitle(col)
        