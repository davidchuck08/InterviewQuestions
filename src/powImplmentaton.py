#!/usr/bin/python

def myPow(x,n):
    if n == 0:
        return 1
    if n < 0:
        return 1/myPow(x,-n)
    if n %2:
        return myPow(x*x, n/2)*x
    else:
        return myPow(x*x, n/2)
    
x=3
n=5
print myPow(x, n)