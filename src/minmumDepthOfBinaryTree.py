#!/usr/bin/python
import sys
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
        self.depth=1
        
def minDepth(root):
    stack=[]
    stack.append(root)
    mindepth=sys.maxint
    while len(stack) >0:
        node=stack.pop()
        if node.left is None and node.right is None:
            if mindepth > node.depth:
                mindepth = node.depth
        if node.left is not None:
            node.left.depth+=node.depth
            stack.append(node.left)
        if node.right is not None:
            node.right.depth+=node.depth
            stack.append(node.right)
    return mindepth

root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.right =Node(3)
root.right.right = Node(3)
root.right.right.right = Node(5)

print minDepth(root)