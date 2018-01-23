#!/usr/bin/python
from Tkconstants import LEFT

class BinarySearch():
    def __init__(self, sortedArray):
        self.sortedArray=sortedArray
        
    def findTarget(self, target):
        if self.sortedArray is None or len(self.sortedArray) == 0:
            return 'array is None'
        if target is None:
            return 'target is None'
        left =0
        right=len(self.sortedArray)-1
        while left+1 < right:
            mid = left+(right-left)/2
            if target == self.sortedArray[mid]:
                left= mid
            elif target > self.sortedArray[mid]:
                left = mid
            else:
                right = mid
        if self.sortedArray[left]==target:
            return left       
        if self.sortedArray[right]==target:
            return right
        
        return None
    
'''   
class BinarySearch:
    def __init__(self, sortedArray):
        self.sortedArray = sortedArray
        
    def findTarget(self, target):
        if self.sortedArray is None or len(self.sortedArray)==0:
            print 'array is None'
            return None
        if target is None:
            print 'target is None'
            return None
        start = 0 
        end = len(self.sortedArray)-1
        
        while  start+1<end :
            mid = start+(end-start)/2
            if self.sortedArray[mid] == target:
                start = mid
            elif self.sortedArray[mid] < target:
                start = mid
            else:
                end = mid
        if self.sortedArray[end] == target:
            print 'end'
            return end
        
        if self.sortedArray[start] == target:
            print 'start'
            return start
        
        if self.sortedArray[end] == target:
            print 'end'
            return end
        
        return None
'''   
if __name__ == '__main__':
    nums = [1,2,3,3,3,4,5,10]
    target = 3
    
    search = BinarySearch(nums)
    print search.findTarget(target)
    
        