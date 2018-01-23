#!/usr/bin/python


def validPalindrome(str):
    if len(str) ==0:
        return False
    if len(str) <2:
        return True
    
    left = 0
    right = len(str)-1
    
    while left< right:
        while str[left].isalpha() == False:
            left+=1
        while not str[right].isalpha():
            right-=1
        if str[left].lower() != str[right].lower():
            return False
        left+=1
        right-=1
    return True

str = "Red rum, sir, is murder"
print validPalindrome(str)
    