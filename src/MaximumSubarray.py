#!/usr/bin/python
import sys
def maximumSubarray(array):
    if array is None or len(array) == 0:
        return 0
    min = -sys.maxint+1
    sum = [min for i in range(len(array))]
    sum[0] = array[0]
    res = -sys.maxint+1
    
    for i in range(1,len(array)):
        sum[i] = max(array[i], sum[i-1]+array[i])
        res = max(res, sum[i])
    
    return res

array =[-2,1,-3,4,-1,2,1,-5,4]
print maximumSubarray(array)