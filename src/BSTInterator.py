#!/usr/bin/python

class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left

class BTIterator():
    def __init__(self,root):
        self.stack=[]
        node=root
        while node is not None:
            self.stack.append(node)
            node=node.left
    def hasNext(self):
        if len(self.stack)>0:
            return True
        return False
    
    def next(self):
        if len(self.stack) ==0:
            return None
        node=self.stack.pop()
        res = node.value
        if node.right is not None:
            node = node.right
            while node is not None:
                self.stack.append(node)
                node=node.left
        return res
    
root = Node(5)
root.left = Node(3)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(4)
iterator = BTIterator(root)
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()