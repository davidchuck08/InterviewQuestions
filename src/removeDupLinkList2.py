#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
def removeDuplist2(root):
    if root is None:
        return None
    head = Node(0)
    head.next=root
    p = head
    while p.next is not None and p.next.next is not None:
        if p.next.value == p.next.next.value:
            dup = p.next.value
            while p.next is not None and p.next.value == dup:
                p.next = p.next.next
        else:
            p=p.next
    return head.next
root=Node(1)
root.next=Node(1)
root.next.next=Node(1)
root.next.next.next=Node(3)
root.next.next.next.next=Node(3)

head = removeDuplist2(root)
while head is not None:
    print head.value
    head=head.next