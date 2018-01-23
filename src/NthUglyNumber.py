#!/usr/bin/python

def getNthUglyNumber(n):
    if n is None:
        return 0
    if n<=0:
        return 0
    
    list=[]
    list.append(1)
    i=0
    j=0
    k=0
    while len(list)<n:
        m2=list[i]*2
        m3=list[j]*3
        m5=list[k]*5
        
        minNum = min(m2, min(m3,m5))
        if minNum == m2:
            i+=1
        if minNum ==m3:
            j+=1
        if minNum ==m5:
            k+=1
        list.append(minNum)
    return list 

n=10
print getNthUglyNumber(n)