#!/usr/bin/python

class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
        
def removeLinkedList(root,target):
    if root is None:
        return None
    fakeNode = Node(0)
    fakeNode.next=root
    p = fakeNode
    while p.next is not None:
        next= p.next
        if next is not None and next.value == target:
            p.next=next.next
        else:
            p=p.next
    return fakeNode.next

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)

head=removeLinkedList(root, 3)
while head is not None:
    print head.value
    head=head.next
            