#!/usr/bin/python

def maxmumProductArray(array):
    if array is None or len(array) == 0:
        return 0
    minVal = [0 for i in range(len(array))]
    maxVal = [0 for i in range(len(array))]
    minVal[0]=maxVal[0] = array[0]
    result = array[0]
    for i in range(1,len(array)):
        if array[i] > 0:
            maxVal[i] = max(array[i], maxVal[i-1]*array[i])
            minVal[i] = min(array[i], minVal[i-1]*array[i])
        else:
            maxVal[i] = max(array[i], minVal[i-1]*array[i])
            minVal[i] = min(array[i], maxVal[i-1]*array[i])
        result = max(result, maxVal[i])
    return result

array = [2,2,3,-2,4]
print maxmumProductArray(array)