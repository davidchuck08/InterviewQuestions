#!/usr/bin/python
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
        
def isSymmetric(l, r):
    if l is None and r is None:
        return True
    if l is None or r is None:
        return False
    if l.value != r.value:
        return False
    if isSymmetric(l.left,l.right) is not True:
        return False
    if isSymmetric(r.left,r.right) is not True:
        return False
    return True

root = Node(1)
root.left =Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(3)
root.right.left=Node(3)
root.right.right=Node(3)
print isSymmetric(root.left, root.right)
    