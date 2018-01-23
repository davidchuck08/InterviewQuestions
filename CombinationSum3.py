#!/usr/bin/python

class CombinationSum3():
    def __init__(self, maxNum, target):
        self.maxNum=maxNum
        self.target=target
        self.candidates=[9,8,7,6,5,4,3,2,1]
        self.result=[]
        
        
    def dfs(self,target,start,valueList):
        if target==0:
            if len(valueList) == self.maxNum:
                self.result.append(valueList)
            return 
        for i in range(start, len(self.candidates)):
            if target < self.candidates[i]:
                continue
            self.dfs(target-self.candidates[i], i, valueList+[self.candidates[i]])
            
    def getCombinationSum(self):
        self.dfs(self.target, 0, [])
        
candidates = [2,3,6,7]
target=7
com=CombinationSum3(3, target)
com.getCombinationSum()
print 'result:' +str(com.result)