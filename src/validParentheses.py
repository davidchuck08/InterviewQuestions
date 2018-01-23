#!/usr/bin/python

def validParentheses(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '{' or str[i] == '[':
            stack.append(str[i])
            
        if str[i] == ')' or str[i] == '}' or str[i] == ']':
            if len(stack) < 1:
                return False
            pre = stack.pop()
            if str[i] == '(' and pre != ')':
                return False
            if str[i] == '{' and pre != '}':
                return False
            if str[i] == '[' and pre != ']':
                return False
    
    return True


str = '{[x+(y+x)-v]}'

print validParentheses(str)