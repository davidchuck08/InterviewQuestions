#!/usr/bin/python
class Node():
    def __init__(self,value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right


def invert(root):
    if root is None:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp
    if root.left is not None:
        invert(root.left)
    if root.right is not None:
        invert(root.right)
def invertBinaryTree(root):
    invert(root)
    return root

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)

root2=invertBinaryTree(root)
print root2.value
print root2.left.value
print root2.right.value
print root2.left.left.value
if root2.left.right is None:
    print None
else:
    print root2.left.right.value

if root2.right.left is None:
    print None
else:
    print root2.right.left.value
print root2.right.right.value
