#!/usr/bin/python

class Palindrome():
    def __init__(self, str):
        self.str = str
        self.minCut = [i-1 for i in range(len(str)+1)]
        
    def isPalindrome(self, str): 
        left=0
        right=len(str)-1
        while left < right:
            if str[left]!=str[right]:
                return False
            left+=1
            right-=1
        return True

    def findMinCut(self):
        for i in xrange(len(self.str)+1):
            for j in xrange(i):
                if self.isPalindrome(self.str[j:i]):
                    self.minCut[i] = min(self.minCut[i], self.minCut[j]+1)
        print self.minCut
        return self.minCut[-1]
str='aabb'  
p = Palindrome(str)
print p.findMinCut()