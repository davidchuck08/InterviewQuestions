#!/usr/bin/python
res=[]
def isPalindrome(str):
    left = 0
    right = len(str)-1
    while(left < right):
        if str[left] != str[right]:
            return False
        left+=1
        right-=1
    return True

def allPalindrome(str):
    if str == None or len(str)==0:
        return None
    result = []
    for i in range(1,len(str)+1):
        if isPalindrome(str[:i]):
            if str[:i] not in res:
                res.append(str[:i])
            allPalindrome(str[i:])
            
str = 'aaabbbaaa'
allPalindrome(str)
print res