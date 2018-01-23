#!/usr/bin/python

def partition(aList, first, last):
        pivot=aList[first]
        left=first+1
        right=last
        print "pivot = %d" %pivot
        print 'left  = %d' %left
        print 'right = %d'  %right
        done=False
        while not done:
            while left<=right and aList[left] <= pivot:
                left+=1
            while aList[right]>=pivot and left <= right :
                right-=1
            
            if right < left:
                done=True
            else:
                temp = aList[left]
                aList[left]=aList[right]
                aList[right]=temp
        print aList
        aList[first]=aList[right]
        aList[right]=pivot
        
        return right
               
            
        

def quickSortHelper(aList, first, last):
    if first < last:
        splitPoint=partition(aList, first, last)  
    
        quickSortHelper(aList, first, splitPoint-1)
        quickSortHelper(aList, splitPoint+1, last)
    return aList
    
def quickSort(aList):
    return quickSortHelper(aList, 0, len(aList)-1)
    
    
aList = [1,40, 39, 42, 79, 100,4, 50000,123]
print quickSort(aList)
