#!/usr/bin/python

def verifyPreorder(preorder):
    list=preorder.split(",")
    stack=[]
    
    for item in list:
        stack.append(item)
        
        while len(stack) >=3 and stack[-1]=='#' and stack[-2]=='#' and stack[-3]!='#':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('#')
    if len(stack)==1 and stack[0]=='#':
        return True
    return False


preorder="9,3,4,#,#,1,#,#,2,#,6,#,#"
print verifyPreorder(preorder)