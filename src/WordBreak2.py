#!/usr/bin/python

class wordBreak2():
    def __init__(self, str, dict):
        self.str=str
        self.dict = dict
        self.dp = [False for x in range(len(str)+1)]
        self.res=[]
    def check(self, s):
        self.dp[0] = True
        for i in range(len(str)+1):
            for j in range(i):
                if self.dp[j] and s[j:i] in self.dict:
                    self.dp[i]=True
        return self.dp[len(self.str)]
    
    def dfs(self, s, stringList):
        if self.check(s):
            if len(s) ==0:
                self.res.append(stringList[1:])
            for i in range(len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:], stringList+' '+s[:i])
str='catsanddog'
dict=["cat", "cats", "and", "sand", "dog"]

sol = wordBreak2(str, dict)
sol.dfs(str,"")
print sol.res