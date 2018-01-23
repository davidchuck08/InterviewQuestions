#!/usr/bin/python

def MergeSort(aList):
    if len(aList) >1:
        mid = len(aList)/2
        leftArray=aList[:mid]
        rightArray=aList[mid:]
        
        MergeSort(leftArray)
        MergeSort(rightArray)
        
        
        leftIndex=0
        rightIndex=0
        totalIndex=0
        
        while leftIndex < len(leftArray) and rightIndex < len(rightArray):
            if leftArray[leftIndex] <= rightArray[rightIndex]:
                aList[totalIndex]=leftArray[leftIndex]
                totalIndex+=1
                leftIndex+=1
            else:
                aList[totalIndex]=rightArray[rightIndex]
                totalIndex+=1
                rightIndex+=1
        while leftIndex<len(leftArray):
            aList[totalIndex]=leftArray[leftIndex]
            totalIndex+=1
            leftIndex+=1
        while rightIndex<len(rightArray):
            aList[totalIndex]=rightArray[rightIndex]
            totalIndex+=1
            rightIndex+=1
    return aList


aList = [1,10,8,100,59,39,56]
print MergeSort(aList)