#!/usr/bin/python

#!/usr/bin/python
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom. For example, given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     
  5             <---
You can see [1, 3, 5].
'''

class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def rightSideView(root):
    if root is None:
        return None
    stack=[]
    stack.append(root)
    res=[]
    while len(stack) >0:
        for i in range(len(stack)):
            node=stack.pop(0)
            if i==0:
                res.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    return res


'''
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def rightSideView(root):
    if root is None:
        return None
    stack=[]
    res=[]
    stack.append(root)
    while len(stack)>0:
        for i in range(len(stack)):
            node = stack.pop(0)
            if i==0:
                res.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    return res
'''
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(5)
print rightSideView(root)