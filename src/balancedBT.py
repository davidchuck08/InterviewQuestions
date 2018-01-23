#/usr/bin/python
'''
Given a binary tree, determine if it is height-balanced.

For this problem, 
a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node 
never differ by more than 1.
'''
class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def getHeight(root):
    if root is None:
        return 0
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    if leftHeight ==-1 or rightHeight==-1:
        return -1
    if abs(leftHeight-rightHeight) >1:
        return -1
    return max(leftHeight, rightHeight)+1

def isBalancedBT(root):
    if getHeight(root) ==-1:
        return False
    return True


'''
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def getHeight(root):
    if root is None:
        return 0
    
    leftHeight=getHeight(root.left)
    rightHeight=getHeight(root.right)
    
    if leftHeight == -1 or rightHeight == -1:
        return -1
    
    if abs(leftHeight-rightHeight) >1 :
        return -1
    return max(leftHeight,rightHeight)+1

def isBalancedBT(root):
    
    height = getHeight(root)
    if height == -1:
        return False
    return True
'''
root = Node(0)
root.left = Node(1)
root.right=Node(2)
root.left.left=Node(3)
print isBalancedBT(root)