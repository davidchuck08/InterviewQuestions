#!/usr/bin/python
import sys
class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def validateBST(root, min, max):
    if root is None:
        return True
    if root.value <= min or root.value >= max:
        return False
    
    return validateBST(root.left, min, root.value) & validateBST(root.right, root.value, max)

root =Node(2)
root.left = Node(1)
root.right =Node(3)
#root.left.left=Node(4)
#root.right.right = Node(5)

print validateBST(root, -sys.maxint-1, sys.maxint)