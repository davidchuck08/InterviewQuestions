#!/usr/bin/python

class Subset():
    def __init__(self, nums):
        self.nums = nums
        self.res = []
    
    def dfs(self, start, valueList):
        dup = sorted(valueList)
        if dup not in self.res :
            self.res.append(dup)
        if len(valueList) == len(self.nums):
            return
        for i in range(start, len(self.nums)):
            self.dfs(i+1, valueList+[self.nums[i]])
    def getSubset(self):
        self.dfs(0,[])
    
nums=[1,2,3]
subset=Subset(nums)
subset.getSubset()
print subset.res