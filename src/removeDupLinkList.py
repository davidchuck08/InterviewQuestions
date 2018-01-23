#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
def removeDuplist(root):
    if root is None:
        return None
    p1=root
    p2=root.next
    
    while p2 is not None:
        if p1.value == p2.value:
            p1.next=p2.next
            p2=p2.next
        else:
            p1.next=p2
            p1=p1.next
            p2=p2.next
    return root

root=Node(1)
root.next=Node(1)
root.next.next=Node(1)
root.next.next.next=Node(3)
root.next.next.next.next=Node(3)

head = removeDuplist(root)
while head is not None:
    print head.value
    head=head.next