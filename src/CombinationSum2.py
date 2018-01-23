#!/usr/bin/python
'''
Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T. 
Each number in C may only be used ONCE in the combination.

Note:
1) All numbers (including target) will be positive integers.
2) Elements in a combination must be in non-descending order.
3) The solution set must not contain duplicate combinations.
'''
class CombinationSum2():
    def __init__(self, candidates, target):
        self.candidates=sorted(candidates, reverse=True)
        self.target=target
        self.res=[]
        
    def dfs(self, target, start, valueList):
        if target==0:
            self.res.append(valueList)
        for i in range(start, len(self.candidates)):
            if target < self.candidates[i]:
                continue
            self.dfs(target-self.candidates[i], i+1, valueList+[self.candidates[i]])

    def getCombinationSum(self):
        self.dfs(self.target,0,[])      




'''
class CombinationSum2():
    def __init__(self, candidates,target):
        self.candidates = sorted(candidates, reverse=True)
        self.target=target
        self.result=[]
    def dfs(self, target, start, valueList):
        for i in range(start, len(self.candidates)):
            if target == 0:
                self.result.append(valueList)
                return
            if self.candidates[i] > target:
                continue
            self.dfs(target-self.candidates[i], i+1, valueList+[self.candidates[i]])
    def getCombinationSum(self):
        self.dfs(self.target, 0, [])
'''      
candidates = [2,3,6,7]
target=7
com=CombinationSum2(candidates, target)
com.getCombinationSum()
print 'result:' +str(com.res)