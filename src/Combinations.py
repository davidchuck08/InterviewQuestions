#!/usr/bin/python
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example, if n = 4 and k = 2, a solution is:
 [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Combinations():
    def __init__(self, n, k):
        self.n=n
        self.k=k
        self.candidates=self.generateCandidateList()
        self.res=[]
        
    def generateCandidateList(self):
        res=[]
        for i in range(1,self.n+1):
            res.append(i)
        return res
    
    def dfs(self, start, valueList):
        if len(valueList) == self.k:
            self.res.append(valueList)
        for i in range(start, len(self.candidates)):
            self.dfs(i+1, valueList+[self.candidates[i]])




'''
class Combinations():
    def __init__(self, n, k):
        self.n=n
        self.k=k
        self.candidates = self.generateCandidateList(self.n)
        self.res=[]
        
    def generateCandidateList(self,n):
        res = []
        for i in range(n,0,-1):
            res.append(i)
        return res

    def dfs(self, start, valueList):
        if len(valueList)==self.k:
            self.res.append(valueList)
            return
        for i in range(start, len(self.candidates)):
            self.dfs(i+1, valueList+[self.candidates[i]])
   
'''     
n=4
k=3

com = Combinations(n,k)
com.dfs(0,[])
print com.res