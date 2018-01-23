#!/usr/bin/python
class Node():
    def __init__(self,value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        
def build(inorder, inStart, inEnd, postorder, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd: 
        return None
    root= Node(postorder[postEnd])
    rootIndex = 0
    for index in range(len(inorder)):
        if inorder[index] == root.value:
            rootIndex=index
            break
    root.left = build(inorder,inStart,rootIndex,postorder,postStart, postStart+rootIndex-inStart-1)
    root.right=build(inorder,rootIndex+1,inEnd, postorder,postStart+rootIndex-inStart,postEnd-1) 
    
    return root   
def constructTree(inorder, postorder):
    inStart =0
    inEnd = len(inorder)-1
    postStart = 0
    postEnd=len(postorder)-1
    return build(inorder,inStart,inEnd,postorder,postStart,postEnd)

inorder= [4,2,5,1,6,7,3,8]
postorder=[4,5,2,6,7,8,3,1]

root=constructTree(inorder, postorder)
print root.value, root.left.value, root.right.value
    
