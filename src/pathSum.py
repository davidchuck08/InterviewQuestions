#!/usr/bin/python


class Node():
    def __init__(self,value, left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
        self.sum=value
        self.path=[value]
        
def pathSum(root, target):
    if root is None:
        return False
    stack =[]
    stack.append(root)
    res=[]
    while len(stack) >0:
        node = stack.pop()
        if node.left is None and node.right is None and node.sum == target :
            res.append(node)
        if node.left is not None:
            node.left.sum += node.sum
            node.left.path= node.path + node.left.path
            stack.append(node.left)
        if node.right is not None:
            node.right.sum +=node.sum
            node.right.path= node.path + node.right.path
            stack.append(node.right)
    return res

root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.right.right = Node(3)

res = pathSum(root, 7)
if res is None:
    print False
else:
    print True
    for x in res:
        print x.path
        
            