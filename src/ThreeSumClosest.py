#!/usr/bin/python
import sys
def threeSumClosest(array, target):
    lastDiff = sys.maxint
    lastI=-1
    lastJ=-1
    lastK=-1
    if len(array)<3: 
        return
    array=sorted(array)
    for i in range(len(array)):
        j=i+1
        k=len(array)-1
        while j<k:
            num = array[i]+array[j]+array[k]
            diff = abs(num-target)
            if diff == 0:
                return diff, array[i],array[j],array[k]
            if diff < lastDiff:
                lastDiff = diff
                lastI = i
                lastJ = j
                lastK = k
            if num <=target:
                j+=1
            else:
                k-=1
    return lastDiff, array[lastI], array[lastJ], array[lastK]

array= [-1,2, 1, -4]
target = 1

print threeSumClosest(array, target)
                
            