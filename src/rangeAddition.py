#!/usr/bin/python

def rangeAddition(length, operations):
    if length <=0:
        return None
    
    arr = [0]*length
    for operation in operations:
        start=operation[0]
        end=operation[1]
        inc=operation[2]
        if start < length:
            arr[start]+=inc
        if end < length-1:
            arr[end+1]-=inc
    
    for i in range(1,length):
        arr[i]+=arr[i-1]
    return arr

operations=[]
operations.append([1,3,2])
operations.append([2,4,3])
operations.append([0,2,-2])
operations.append([5,5,-3])
print rangeAddition(5, operations)