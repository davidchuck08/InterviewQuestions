#!/usr/bin/python
'''
Given a set of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T. 
The same repeated number may be chosen from C unlimited number of times.

Note: All numbers (including target) will be positive integers. 
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak). 
The solution set must not contain duplicate combinations. 
For example, given candidate set 2,3,6,7 and target 7, A solution set is:
 [7] 
[2, 2, 3] 
'''
import copy
class CombinationSum():
    def __init__(self, candidates, target):
        self.candidates=sorted(candidates, reverse=True)
        self.target=target
        self.res=[]
    def dfs(self, target, start, valueList):
        if target==0:
            self.res.append(valueList)
            return
        for i in range(start, len(self.candidates)):
            if target < self.candidates[i]:
                continue
            self.dfs(target-self.candidates[i], i, valueList+[self.candidates[i]])

    def getCombinationSum(self):
        self.dfs(self.target, 0, [])




'''
import copy
class CombinationSum():
    def __init__(self, candidates, target):
        self.candidates=sorted(candidates, reverse=True)
        self.target=target
        self.result=[]
    def dfs(self, target, start, valueList):
        print target, valueList
        if target ==0:
            self.result.append(valueList)
            return
        
        for i in range(start, len(self.candidates)):
            if target < self.candidates[i]:
                print 'return: %d %d' %(target, self.candidates[i])
                continue
            print 'append %d' %self.candidates[i]
            self.dfs(target-self.candidates[i], i,valueList+[self.candidates[i]])
            print 'curr' + str(valueList)
    def getCombinationSum(self): 
        target = self.target
        self.dfs(target, 0, [])
'''
candidates = [2,3,6,7]
target=7
candidates.sort()
com=CombinationSum(candidates, target)
com.getCombinationSum()
print 'result:' +str(com.res)