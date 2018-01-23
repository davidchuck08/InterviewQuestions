#!/usr/bin/python
import collections
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
        self.height=0
        self.rightPointer=None
        
def populateNextRight(root):
    stack=[]
    res=collections.defaultdict(list)
    stack.append(root)
    while len(stack)>0:
        node=stack.pop()
        res[node.height].append(node)
        if node.right is not None:
            node.right.height=node.height+1
            stack.append(node.right)
        if node.left is not None:
            node.left.height=node.height+1
            stack.append(node.left)
    for key in res:
        array=res[key]
        for i in range(len(array)-1):
            array[i].rightPointer=array[i+1]
    return res
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
res = populateNextRight(root)
for node in res[1]:
    print '----'
    print node.value
    print node.left.value
    print node.right.value
    if  node.rightPointer is not None:
        print node.rightPointer.value
    else:
        print None