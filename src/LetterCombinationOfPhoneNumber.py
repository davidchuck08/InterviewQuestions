#!/usr/bin/python

class LetterCombinationOfPhoneNumber():
    def __init__(self):
        self.map={}
        self.map['2']='abc'
        self.map['3']='def'
        self.map['4']='ghi'
        self.map['5']='jkl'
        self.map['6']='mno'
        self.map['7']='pqrs'
        self.map['8']='tuv'
        self.map['9']='wxyz'
        self.result=[]
        
    
    def generateLetterCombination(self, str):
        if str is None or len(str) ==0:
            return None
        self.dfs(0,str,[],len(str))
        
    def dfs(self, start, str, valueList, finalLen):   
        if len(valueList) == finalLen:
            self.result.append(valueList)
            return
        
        for i in range(start, finalLen):
            for k in self.map[str[i]]:
                self.dfs(i+1,str,valueList+[k], finalLen)
                
str = '23'
com = LetterCombinationOfPhoneNumber()
com.generateLetterCombination(str)   
print com.result   