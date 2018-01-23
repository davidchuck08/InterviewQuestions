#!/usr/bin/python

'''
Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.
'''

import heapq


class MedianFinder():
    def __init__(self):
        self.maxHeap=[]
        self.minHeap=[]
        
    def addNum(self,num):
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap,-num))
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, num))
    
    def getMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap[0]-self.minHeap[0])/2.0
        else:
            return self.maxHeap[0]
            
            
    
    
    
    
    
'''
class MedianFinder():
    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        
    def addNum(self,num):
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, -num))
        else:
            heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap, num))
        print 'Num: %d' %num
        print 'maxHeap: ' +str(self.maxHeap)
        print 'minHeap: ' +str(self.minHeap)
        
    def getMedian(self):
        print self.minHeap
        print self.maxHeap
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.minHeap[0]+self.maxHeap[0])/2.0
        else:
            return self.maxHeap[0]
'''       
finder= MedianFinder()

finder.addNum(1)
finder.addNum(10)
finder.addNum(100)
finder.addNum(5)
finder.addNum(20)
print finder.getMedian()