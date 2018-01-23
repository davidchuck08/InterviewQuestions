#!/usr/bin/python

'''
Divide two integers without using multiplication, division and mod operator. If it is overflow, return MAX_INT.
'''
def divideTwoInteger(dividend, divisor):
    if dividend is None or divisor is None:
        return 'error'
    if divisor == 0:
        return 0
    if dividend == 0:
        return 0
    res = 0
    negative=False
    if dividend>0 and divisor<0:
        negative=True
    if dividend<0 and divisor>0:
        negative=True
    dividend=abs(dividend)
    divisor=abs(divisor)  
    while dividend >= divisor:
        numShift=0
        while dividend>=divisor<<numShift:
            numShift+=1
        res+=1<<numShift-1
        dividend-=divisor<<numShift-1
    if negative is True:
        return -res
    return res
        
'''
def divideTwoInteger(dividend, divisor):
    if dividend == 0:
        return 0
    if divisor == 0:
        return 'Error'
    
    negative = False
    if dividend<0 and divisor>0:
        negative=True
    if dividend>0 and divisor<0:
        negative=True
    absDividend = abs(dividend)
    absDivisor = abs(divisor)
    res=0
    while absDividend >= absDivisor:
        numShift=0
        while absDividend>=absDivisor << numShift:
            numShift+=1
        res+=1 << numShift-1
        absDividend-=absDivisor << numShift-1
    
    if negative:
        return -res
    return res
 
'''

dividend = 100
divisor = 4

print divideTwoInteger(dividend, divisor)