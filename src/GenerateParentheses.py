#!/usr/bin/python


'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
 "((()))", "(()())", "(())()", "()(())", "()()()"
'''
class ParenthesesCombination():
    def __init__(self,n):
        self.left=n
        self.right=n
        self.res=[]
    
    def dfs(self, left, right, valueStr):
        if left > right:
            return
        if left ==0 and right==0:
            self.res.append(valueStr)
        if left > 0:
            valueStr+='('
            self.dfs(left-1, right, valueStr)
        if right >0:
            valueStr+=')'
            self.dfs(left, right-1,valueStr)
    def getAllCombination(self):
        self.dfs(self.left, self.right, '')
        return self.res
            
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
''' 
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
'''
com = ParenthesesCombination(3)
print com.getAllCombination()
