#!/usr/bin/python
'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given
          1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''


class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        
class Flatter():
    def __init__(self,root):
        self.root=root
        self.queue=[]
    
    def flatBt(self, node):
        if node is None:
            return None
        
        self.queue.append(node.value)
        if node.left is not None:
            self.flatBt(node.left)
        if node.right is not None:
            self.flatBt(node.right)
    
    















'''
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def flattenBST(root, queue):
    if root is None:
        return
    queue.append(root)
    if root.left is not None:
        flattenBST(root.left, queue)
    if root.right is not None:
        flattenBST(root.right,queue)
    
    return queue
'''
root =Node(1)
root.left = Node(2)
root.right =Node(5)

flatter = Flatter(root)
flatter.flatBt(root)
print flatter.queue
'''
queue=[]

res = flattenBST(root, queue)
length= len(res)
for index in range(length):
    if index < length-1:
        print "%d ->" %res[index].value,
    else:
        print "%d" %res[index].value
'''