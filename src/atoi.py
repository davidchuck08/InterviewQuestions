#!/usr/bin/python

'''
Convert String to integer
'''
def atoi(str):
    if str is None or len(str) == 0:
        return 0
    negative = False
    res=0
    for i in range(len(str)):
        if i ==0 and str[i] == '-':
            negative=True
        else:
            if str[i]<'0' or str[i] >'9':
                return 'wrong input'
            res=res*10+int(str[i])
    return res
                
'''
def atoi(str):
    negative = False #negative flag
    if len(str) == 0:
        return 0
    res = 0
    for i in range(len(str)):
        if i == 0 and str[i] == '-':
            negative = True
        else:
            if str[i] >= '0' and str[i] <= '9':
                res = 10*res + (ord(str[i])-ord('0'))
            else:
                print 'wrong input' 
                return
    if negative:
        res = -1 * res
    return res
'''
str = '145'

print atoi(str)        
    
    