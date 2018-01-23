#!/usr/bin/python
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
     3
   / \
  9  20
    /  \
   15   7
   
return its level order traversal as [[3], [9,20], [15,7]]
'''
class Node():
    def __init__(self,value, left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def binaryTreeLevelOrderTravelsal(root):
    if root is None:
        return None
    current=[]
    next=[]
    levelRes=[]
    finalRes=[]
    current.append(root)
    while len(current) > 0:
            node=current.pop()
            if node.left is not None:
                next.append(node.left)
            if node.right is not None:
                next.append(node.right)
            levelRes.append(node.value)
            if len(current) == 0:
                current=next
                next=[]
                finalRes.append(levelRes)
                levelRes=[]
    return finalRes        
'''
def binaryTreeLevelOrderTravelsal(root):
    if root is None:
        return 
    current = []
    next = []
    finalRes=[]
    levelRes = []
    
    current.append(root)
    while len(current) > 0:
        node=current.pop()
        if node.right is not None:
            next.append(node.right)
        if node.left is not None:
            next.append(node.left)
        levelRes.append(node.value)
        if len(current)  == 0:
            current = next
            next = []
            finalRes.append(levelRes)
            levelRes = []
    return finalRes
'''
def binaryTreeLevelOrderTravelsal2(root):
    if root is None:
        return 
    current = []
    next = []
    finalRes=[]
    levelRes = []
    
    current.append(root)
    while len(current) > 0:
        node=current.pop()
        if node.right is not None:
            next.append(node.right)
        if node.left is not None:
            next.append(node.left)
        levelRes.append(node.value)
        if len(current)  == 0:
            current = next
            next = []
            finalRes.append(levelRes)
            levelRes = []
    return finalRes[::-1]

root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.right.right = Node(5)

print binaryTreeLevelOrderTravelsal(root)
print binaryTreeLevelOrderTravelsal2(root)
            