#!/usr/bin/python

class Node():
    def __init__(self,value,left=None,right=None):
        self.val=value
        self.left=left
        self.right=right
def lowestCommonAncentor(root,node1,node2):

    if (node1.val > root.val and node2.val < root.val) or (node1.val < root.val and node2.val > root.val):
        return root
    if node1.val < root.val and node2.val < root.val:
        if root.left is not None:
            return lowestCommonAncentor(root.left, node1, node2)
    if node1.val > root.val and node2.val > root.val:
        if root.right is not None:
            return lowestCommonAncentor(root.right, node1, node2)
    return root
root=Node(5)
root.left=Node(3)
root.left.left=Node(1)
root.left.right=Node(4)
root.right=Node(7)
root.right.left=Node(6)

node1=Node(1)
node2=Node(6)

ancentor = lowestCommonAncentor(root, node1, node2)
print ancentor.val
