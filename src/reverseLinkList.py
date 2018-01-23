#!/usr/bin/pyhon

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        
def reverse(head):
    pre = head
    curr = head.next
    while curr is not None:
        temp = curr.next
        curr.next = pre
        pre = curr
        curr = temp
    head.next=None
    return pre

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)

linklist = head
while linklist is not None:
    print linklist.val
    linklist=linklist.next
    
reversed = reverse(head)
while reversed is not None:
    print reversed.val
    reversed=reversed.next