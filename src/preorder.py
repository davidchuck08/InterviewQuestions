#!/usr/bin/python
class Node():
    def __init__(self,value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def Preorder(root):
    result = []
    result.append(root.value)
    if root.left is not None:
        result = result + Preorder(root.left)
    if root.right is not None:
        result = result + Preorder(root.right)
    return result
    
root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.right.right = Node(5)

print Preorder(root)
        