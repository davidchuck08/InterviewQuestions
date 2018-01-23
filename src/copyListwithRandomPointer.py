#!/usr/bin/python
'''
A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
        self.random=None
        
        
def deepCopy(root):
    node=root
    while node is not None:
        temp = node.next
        node.next=Node(node.value)
        node.next.next=temp
        node=node.next.next
   
    node=root
    while node is not None:
        if node.random is not None:
            node.next.random=node.random.next
        node=node.next.next
    
    oldHead=root
    newHead=root.next
    while oldHead is not None:
        temp=oldHead.next
        oldHead.next=temp.next
        if temp.next is not None:
            temp.next=temp.next.next
        oldHead=oldHead.next
    return newHead
'''
class Node():
    def __init__(self,value):
        self.value = value
        self.next=None
        self.random=None
        
        
def deepCopy(root):
    node = root
    while node is not None:
        temp = node.next
        newNode=Node(node.value)
        node.next=newNode
        newNode.next=temp
        node=temp
    
    node = root
    while node is not None:
        if node.random is not None:
            node.next.random=node.random.next
        node=node.next.next
    oldhead = root
    newhead = root.next
    while oldhead is not None:
        temp = oldhead.next
        oldhead.next = temp.next
        if temp.next is not None:
            temp.next=temp.next.next
        oldhead=oldhead.next
    return newhead    
'''
root = Node(1)
root.next=Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)    

root.next.random = root.next.next.next

dupList=deepCopy(root)  
while dupList is not None:
    print 'value: %d' %dupList.value
    if dupList.random is not None:
        print 'random: %d' %dupList.random.value
    dupList = dupList.next