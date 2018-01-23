#!/usr/bin/python
'''
Given a binary tree, collect a tree's nodes as if you were doing this: 
Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree
           1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

'''
class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

class LeafFinder():
    def __init__(self, root):
        self.root=root
        self.res=dict()
    def findLeaf(self,root):
        if root is None:
            return -1
        left=self.findLeaf(root.left)
        right=self.findLeaf(root.right)
        curr=max(left,right)+1
        if curr not in self.res.keys():
            self.res[curr]=[]
        self.res[curr].append(root.value)
       
            
            
        return curr
 
 
 
  







'''
class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

res={}        
def findLeaf(root):
    
    if root is None:
        return -1
    left=findLeaf(root.left)
    right=findLeaf(root.right)
    curr =max(left,right)+1
    if curr not in res:
        res[curr]=[]
    res[curr].append(root.val)
    return curr
'''

root = Node(3)
root.left=Node(2)
root.right=Node(4)
root.right.right=Node(5)
res = {}

finder=LeafFinder(root)
finder.findLeaf(finder.root)
print finder.res