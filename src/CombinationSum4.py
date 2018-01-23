#!/usr/bin/python
'''
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.
'''
class CombinationSum4():
    def __init__(self, candidates,target):
        self.candidates=candidates
        self.target=target
        self.dp=[0 for i in range(target+1)]
    def getCombination(self):
        self.dp[0]=1
        for i in range(len(self.dp)):
            for candidate in self.candidates:
                if i + candidate >target:
                    continue
                self.dp[i+candidate]+=self.dp[i]
        return self.dp[-1]

    
'''
class CombinationSum4():
    def __init__(self, candidates,target):
        self.candidates=candidates
        self.target=target
        self.dp=[0 for i in range(target+1)]
    
    def getCombination(self):
        self.dp[0]=1
        for i in range(len(self.dp)):
            for candidate in self.candidates:
                if i+candidate <=target:
                    self.dp[i+candidate]+=self.dp[i]
        return self.dp[-1]
    
'''    
candidates = [1,2,4,5]
target = 2
com = CombinationSum4(candidates, target)
print com.getCombination()