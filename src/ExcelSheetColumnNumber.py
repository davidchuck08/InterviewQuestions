#!/usr/bin/python
'''
Given a column title as appear in an Excel sheet, return its corresponding column number. For example:
     A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    AAA -> 703 
'''
def columnNumber(col):
    map=dict()
    start=ord('A')
    for i in range(27):
        map[chr(start+i)]=i+1
    res=0
    for i in range(len(col)):
        res+=map[col[i]]*pow(26,len(col)-1-i)
    return res
        
    












'''
def columnNumber(col):
    #build map
    map = dict()
    start=ord('A')
    for i in range(1,27):
        map[chr(start+i-1)] = i
    totalLen=len(col)
    res =0
    for i in range(totalLen):
        res+=map[col[i]]*pow(26,totalLen-i-1)
    return res
'''
str = 'AAA'
print columnNumber(str)