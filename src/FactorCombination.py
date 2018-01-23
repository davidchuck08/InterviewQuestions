#!/usr/bin/python
'''
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
'''

class  FactorCombination():
    def __init__(self, num):
        self.num=num
        self.res=[]
    def dfs(self, num, factorStr):
        if num is None:
            return None
        if num == 1:
            self.res.append(factorStr[1:])
            
        for i in range(2, num+1):
            if num%i ==0:
                self.dfs(num/i, factorStr+'x'+str(i))
    def factor(self):
        self.dfs(self.num,'')
        

















'''
class FactorCombination():
    def __init__(self, number):
        self.number=number
        self.res=[]
        
    def factor(self):
        self.dfs(self.number,"")
    def dfs(self, num, factorStr):
        if num == 1:
            self.res.append(factorStr[1:])
            return
        for i in range(2,num+1):
            if num % i == 0:
                self.dfs(num/i, factorStr+'x'+str(i))

'''
number = 8
factor = FactorCombination(number)
factor.factor()
print factor.res