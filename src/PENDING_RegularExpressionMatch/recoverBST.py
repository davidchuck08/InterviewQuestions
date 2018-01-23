#!/usr/bin/python

class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def getInorderList(root):
    stack=[]
    res=[]
    if root==None:
        return
    
    current=root
    done = False
    while not done:
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            if len(stack) >0:
                p = stack.pop()
                res.append(p)
                if p.right is not None:
                    stack.append(p.right)
            else:
                done=True
               
    return res   

root=Node(5)
root.left=Node(6)
root.left.left=Node(1)
root.left.right=Node(4)
root.right=Node(3)

inorderList=getInorderList(root)
first = None
second = None
for i in range(len(inorderList)-1):
    if inorderList[i].value > inorderList[i+1].value:
        if first is None:
            first=inorderList[i].value
        else:
            second = inorderList[i+1].value
        
print first,second 