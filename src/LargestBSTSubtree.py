#!/usr/bin/python
import sys
from __builtin__ import True
class Node():
    def __init__(self, val, left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Wrapper():
    def __init__(self):
        self.min=sys.maxint
        self.max=-sys.maxint+1
        self.size=0
        self.isBST=False
def helper(root):
    wrap = Wrapper()
    if root is None:
        wrap.isBST=True
        return wrap
    left = helper(root.left)
    right = helper(root.right)
    wrap.min = min(left.min,root.val)
    wrap.max = max(right.max, root.val)
    if left.isBST is True and right.isBST is True and left.max < root.val and right.min > root.val:
        wrap.isBST=True
        wrap.size=left.size+right.size+1
    else:
        wrap.size=max(left.size,right.size)
        wrap.isBST=False
    return wrap

root = Node(5)
root.left=Node(4)
root.right=Node(6)
root.left.left=Node(3)
root.right.right=Node(7)

wrap=helper(root)
print wrap.size     