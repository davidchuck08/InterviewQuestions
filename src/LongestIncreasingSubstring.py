#!/usr/bin/python
from _ast import Num

def getLongestIncreasingSubsequence(seq):
    res = []
    if seq is None or len(seq) == 0:
        return res
    res.append(seq[0])
    for num in seq:
        if num > res[-1]:
            res.append(num)
        else:
            index=binarySearch(res, num)
            res[index]=num
            
    return res
def binarySearch(seq, num):
    i = 0
    j = len(seq)-1
    while i < j:
        mid = i + (j-i)/2
        if seq[mid] < num:
            i=mid+1
        else:
            j=mid
    return j
seq=[10,9,2,5,3,7,101,18,102]
print getLongestIncreasingSubsequence(seq)