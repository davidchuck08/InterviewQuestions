#!/usr/bin/python
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
        self.RLvalue=value
        
def sumRootToLeaf(root):
    stack=[]
    stack.append(root)
    res = 0
    while len(stack)>0:
        node=stack.pop()
        if node.left is None and node.right is None:
            res+=node.RLvalue
            
        if node.left is not None:
            node.left.RLvalue +=node.RLvalue*10
            stack.append(node.left)
        if node.right is not None:
            node.right.RLvalue+=node.RLvalue*10
            stack.append(node.right)
    return res

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(0)
print sumRootToLeaf(root)