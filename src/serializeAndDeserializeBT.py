#!/usr/bin/python
from fabric.decorators import serial

class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
        self.isLeaf=False


def serialize(root, serializeStr):
    if root is None:
        return
    serializeStr+=str(root.value)
    if root.left is not None:
       serializeStr = serialize(root.left, serializeStr)
    else:
       serializeStr+='#'
    if root.right is not None:
       serializeStr =serialize(root.right, serializeStr)
    else:
       serializeStr+='#'
    return serializeStr
'''
def deserialize(str):
    stack = []
    res = []
    for i in range(len(str)):
        print 'item %d' %i,
        print str[i],
        stack.append(Node(str[i]))
        while len(stack)>3 and (stack[-1].value=='#' or stack[-2].isLeaf) and (stack[-2].value == '#' or stack[-2].isLeaf) and stack[-3].value!='#':
            node = Node(stack[-3].value)
            if stack[-2] != '#':
                node.left=stack[-2]
            if stack[-1] != "#":
                node.right = stack[-1]
            node.isLeaf=True
            if stack[-1].isLeaf is False:
                stack.pop()
            if stack[-1].isLeaf is False:
                stack.pop()
            if stack[-1].isLeaf is False:
                stack.pop()
            stack.append(node)
        print 'stack:',    
        for d in stack:
            print d.value,
        print '----'
    for x in stack:
        print x.value
'''
def deserialize(str, index):
        
        if str[index] == '#':
            return None, index
        root = Node(str[index])
        index+=1
        root.left,index=deserialize(str, index)
        index+=1
        root.right,index =deserialize(str, index)
        
        return root,index
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
serializeStr=""
serializeStr= serialize(root, serializeStr)
print serializeStr

node, index = deserialize(serializeStr,0)
print node.value
print node.left.value
print node.right.value
print node.left.left.value
            