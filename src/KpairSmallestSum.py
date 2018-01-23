#!/usr/bin/python
import heapq,sys
def kpairSmallestSum(num1, num2, k):
    if num1 is None or len(num1)==0 or num2 is None or len(num2) ==0:
        return 'invalid input'
    
    heap=[]
    heap.append((sys.maxint, None, None))
    idx1=0
    size1=len(num1)
    size2=len(num2)
    ans=[]
    k=min(k, size1*size2)
    while len(ans)<k:
        if idx1<len(num1):
            sum, i, j=heap[0]
            if num1[idx1]+num2[0]<sum:
                for idx2 in range(len(num2)):
                    heapq.heappush(heap,(num1[idx1]+num2[idx2], num1[idx1], num2[idx2]))
                idx1+=1
        sum, i, j = heapq.heappop(heap)
        
        ans.append((i,j))
    return ans
num1=[1,7,11]
num2=[2,4,6]
k=100
print kpairSmallestSum(num1, num2,k)