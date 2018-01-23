#!/usr/bin/python
class Node():
    def __init__(self,value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
def build(inorder,inStart, inEnd,preorder, preStart, preEnd):
    if inStart > inEnd or preStart > preEnd:
        return None
    root=Node(preorder[preStart])
    rootIndex=0
    for index in range(len(inorder)):
        if inorder[index]==root.value:
            rootIndex=index
            break
        
    root.left=build(inorder,inStart,rootIndex-1,preorder,preStart+1,preStart+1+rootIndex-inStart-1)
    root.right=build(inorder,rootIndex+1,inEnd, preorder,preStart+rootIndex-inStart+1,preEnd)
    return root
def constructTree(inorder, preorder):
    inStart =0
    inEnd = len(inorder)-1
    preStart = 0
    preEnd=len(preorder)-1
    return build(inorder,inStart,inEnd,preorder,preStart,preEnd)

inorder= [4,2,5,1,6,7,3,8]
postorder=[1,2,4,5,3,7,6,8]

root=constructTree(inorder, postorder)
print root.value, root.left.value, root.right.value