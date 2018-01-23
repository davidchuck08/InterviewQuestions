#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
def partition(root, target):
    if root is None:
        return None
    
    fakeHead1=Node(0)
    fakeHead2=Node(0)
    p=root
    p1=fakeHead1
    p2=fakeHead2
    while p is not None:
        if p.value < target:
            p1.next=p
            p1=p1.next 
        else:
            p2.next=p
            p2=p2.next
            
        p=p.next
    p1.next=fakeHead2.next
    p2.next = None
    return fakeHead1.next


root=Node(1)
root.next=Node(4)
root.next.next=Node(3)
root.next.next.next=Node(2)
root.next.next.next.next=Node(5)
root.next.next.next.next.next=Node(2)

head = partition(root, 3)

while head is not None:
    print head.value
    head=head.next
