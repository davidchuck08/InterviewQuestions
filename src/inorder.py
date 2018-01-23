#!/usr/bin/python
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def printInorder(root):
    res = []
    if root is not None:
        if root.left is not None:
            res = res + printInorder(root.left)
        res.append(root.value)
        if root.right is not None:
            res = res + printInorder(root.right)
            
    return res

root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.right.right = Node(5)

print printInorder(root)