#!/usr/bin/python

def getKthItem( arrayA, arrayB, k):
    lenA = len(arrayA)
    lenB = len(arrayB)
    
    if lenA > lenB: 
        return getKthItem(arrayB, arrayB, k)
    if lenA == 0:
        return arrayB[k-1]
    
    if k == 1:
        return min(arrayA[0], arrayB[0])
    
    pa = min(k/2, lenA)
    pb = k-pa
    
    if arrayA[pa-1] <= arrayB[pb-1]:
        return getKthItem(arrayA[pa:], arrayB, pb)
    else:
        return getKthItem(arrayA, arrayB[pb:], pa)
    

arrayA = [1,3,5,7,9]
arrayB = [2,4,6,8,10,12,14]
totalNum = len(arrayA)+len(arrayB)
if totalNum%2==1:
    print getKthItem(arrayA, arrayB, totalNum/2+1)
else:
    print (getKthItem(arrayA, arrayB, totalNum/2+1)+getKthItem(arrayA, arrayB, totalNum/2))/2