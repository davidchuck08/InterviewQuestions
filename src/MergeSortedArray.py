#!/usr/bin/python

def mergeSortedArray(listA, numA, listB, numB):
    while numA >0 and numB >0:
        if listA[numA-1] > listB[numB-1]:
            listA[numA+numB-1] = listA[numA-1]
            numA-=1
        else:
            listA[numA+numB-1] = listB[numB-1]
            numB-=1
    while numB >0:
        print numA
        print numB
        listA[numA+numB-1] = listB[numB-1]
        numB-=1
    return listA   
        
listA = [1,3,5,7,0,0,0,0]
numA = 4
listB = [2,4,10]
numB=3

print mergeSortedArray(listA, numA, listB, numB)