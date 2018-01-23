import sys
class solution:
    def findMedium(self,listA, listB):
        totalNums = len(listA)+len(listB)
        mediumIndex = totalNums/2
        odd = False
        if totalNums%2 ==1:
            odd = True
            mediumIndex += 1
        index= 0
        startA = 0
        startB = 0
        while index < mediumIndex:
            
            if mediumIndex - index == 1:
                if odd is True:
                    return min(listA[startA], listB[startB])
                else:
                    if listA[startA] < listB[startB]:
                        return (listA[startA]+min(listA[startA+1],listB[startB],listB[startB+1]))/2.0
                    else:
                        return (listB[startB]+min(listB[startB+1],listA[startA],listA[startA+1]))/2.0
                    
            
            midA = startA+(mediumIndex-index)/2
            midB = startB +(mediumIndex-index)/2
            numA = listA[midA]
            numB = listB[midB]
            if midA >= len(listA):
                numA = sys.maxsize
            if midB >=len(listB):
                numB = sys.maxsize
            if numA <numB:
                index+=midA-startA
                startA = midA                
            else:
                index+=midB-startB
                startB=midB
if __name__ == '__main__':
    listA = [1,2,3,5,6]
    listB = [2,3,4,4,10]
     
    sol = solution()
    print sol.findMedium(listA, listB)       