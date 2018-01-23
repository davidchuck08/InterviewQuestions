#!/usr/bin/python
class ParenthesesCombination():
    def __init__(self,n):
        self.left = n
        self.right = n
        self.result = []
        
    def getAllCombination(self):
        self.dfs("", self.left, self.right)
        return self.result
        
    def dfs(self,tempstr, left, right):
        if left > right:
            return
        if left == 0 and right ==0:
            return self.result.append(tempstr)
        if left > 0:
            self.dfs(tempstr+"(",left-1, right)
        if right > 0:
            self.dfs(tempstr+")",left, right-1)
com = ParenthesesCombination(3)
print com.getAllCombination()
