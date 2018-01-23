#!/usr/bin/python
from StdSuites.AppleScript_Suite import result

def minimumSizeSubarraySum(array, target):
    if len(array) == 0:
        return 0
    
    result = len(array)
    sum = 0
    start = 0
    exist = False
    i=0
    while i <= len(array):
        if sum >= target:
            exist = True
            if start == i-1:
                return 1
            result = min (result, i-start)
            sum = sum - array[start]          
            start+=1
        else:
            if i == len(array):
                break
            sum+=array[i]
            i+=1
    if exist:
        return result
    
    return 0

array = [2,3,1,2,4,3]
target = 7

print minimumSizeSubarraySum(array, target)
