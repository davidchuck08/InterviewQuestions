#!/usr/bin/python

def longestConsectiveInBST(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    maxLen=1
    while len(queue) > 0:
        node=queue.pop(0)
        curr=node.value
        if node.left is not None:
            leftLen=0
            if node.left.value==curr+1:
                queue.append(node.left)
                leftLen+=1
                maxLen=max(maxLen,leftLen)
            else:
                leftLen=1
        rightLen=1
        if node.right.value==curr+1:
            queue.append(node.right)
            curr    