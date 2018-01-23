#!/usr/bin/python

class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def isSameTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    if root1.value != root2.value:
        return False
    
    else:
        return isSameTree(root1.left, root2.left) & isSameTree(root1.right, root2.right)
    
    
root1=Node(5)
root1.left=Node(6)
root1.left.left=Node(1)
root1.left.right=Node(4)
root1.right=Node(3)

root2=Node(5)
root2.left=Node(6)
root2.left.left=Node(1)
root2.left.right=Node(4)
root2.right=Node(3)

print isSameTree(root1, root2)