#! /usr/bin/python
from Finder.Finder_items import item

def operation(varA, varB, operator):
    ans = 0
    if operator == "+":
        ans = varA + varB
    elif operator == "-":
        ans = varA - varB
    elif operator == "*":
        ans = varA * varB
    elif operator == "/":
        ans = float(varA) / float(varB)
    else:
        return "ERROR"
    return ans

def reversePolishNotation(input):
    stack = []
    operator = ["+", "-", "*", "/"]
    for item in input:
        if isinstance(item, int):
            stack.append(item)
            print stack
        elif item in operator:
            if len(stack) <= 1:
                print "Ans = %d" %(stack.pop())
                break
            varA = stack.pop()
            varB = stack.pop()
            ans = operation(varA, varB, item)
            print ans 
            if ans ==  "ERROR":
                print "invalid input"
                break
            stack.append(ans)
        
            
        else:
            print "invalid input %s. Skip" %item      
            
input = [1, 3, '/', 4, '+']
reversePolishNotation(input)  