#!/usr/bin/python

def longestValidParaetheses(str):
    maxResult = 0
    currentResult = 0
    stack = []
    
    for i in range(len(str)):
        if str[i] == "(":
            stack.append(str[i])
        if str[i] == ')':
            if len(stack) < 1:
                if currentResult > maxResult:
                    maxResult = currentResult
                    currentResult = 0
            else:
                stack.pop()
                currentResult+=2
    
    return max(currentResult, maxResult)

str = ')((((()))))))'  
print longestValidParaetheses(str)              