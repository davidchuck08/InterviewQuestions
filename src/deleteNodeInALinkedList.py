#!/usr/bin/python
'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, 
the linked list should become 1 -> 2 -> 4 after calling your function.
'''
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

def remove(head, target):
    if target is None or head is None:
        return None
    fakeHead=Node(-1)
    fakeHead.next=head
    p=fakeHead
    while p is not None:
        if p.next is not None and p.next.value==target:
            p.next=p.next.next
        p=p.next
    return fakeHead.next









'''
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
def remove(root, target):
    if root is None:
        return None
    fakeHead = Node(-1)
    fakeHead.next=root
    p = fakeHead
    while p.next is not None:
        if p.next.value == target:
            p.next=p.next.next
        p = p.next
    return fakeHead.next
'''
root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)

head = remove(root, 1)
while head is not None:
    print head.value
    head=head.next