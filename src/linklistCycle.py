#!/usr/bin/python

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
def checkCycle(root):
    slow = root
    fast = root
    
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow.value == fast.value:
            return True
    return False

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)
#root.next.next.next.next.next=root.next.next

print checkCycle(root)