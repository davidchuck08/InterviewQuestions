#!/usr/bin/python

def binary(n):
    if n==0:
        return ''
    else:
        return binary(n/2)+str((n%2))
   
def maxBinaryGap(n):
    str = binary(n)
    maxgap = 0
    gap = 0
    first1 = True
    for i in str:
        if i == '1':
            if first1 is True:
                first1=False
            else:
                if maxgap < gap:
                    maxgap = gap
                    gap=0
        else:
            if first1 is False:
                gap+=1
    return maxgap      
print binary(2)
n=9
print maxBinaryGap(n)