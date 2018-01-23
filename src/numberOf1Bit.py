#!/usr/bin/python
def binary(n):
    if n ==0:
        return ''
    else:
        return binary(n/2)+str(n%2) 
def numberOf1Bit(n):
    str = binary(n)
    count = 0
    for i in str:
        if i =='1':
            count+=1
    return count

n = 5
print numberOf1Bit(n)
    