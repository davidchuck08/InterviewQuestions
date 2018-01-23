#!/usr/bin/python

def searchInserPosition(array, target):
    if len(array) == 0:
        return -1
    if target > array[len(array)-1]:
        return len(array)
    left = 0
    right = len(array)
    
    while left < right:
        mid = (right-left)/2
        if target > array[mid]:
            left = mid+1
        else:
            right = mid
        
    return right

array = [1,3,5,6]
target = 0
print searchInserPosition(array, target)