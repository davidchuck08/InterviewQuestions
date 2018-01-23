#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value=value
        self.next = None
        
def oddEvenLinkList(root):
    if root is None:
        return None
    res = root
    odd = root
    even=root.next
    connectNode = root.next
    
    while odd is not None and even is not None:
        odd.next = even.next
        odd = odd.next
        
        even.next = odd.next
        even=even.next
    odd.next = connectNode
    return res

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)

head=oddEvenLinkList(root)
while head is not None:
    print head.value
    head=head.next
    