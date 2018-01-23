#!/usr/bin/python
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
def reverseLinkedList(root):
    pre = root
    current = root.next
    
    while current is not None:
       
        temp = current.next
        current.next = pre
        pre = current
        current = temp
        
    root.next = None
    
    return pre

def isPalindrome(root):
    reverseRoot= reverseLinkedList(root)
    
    while root is not None:
        if root.value != reverseRoot.value:
            return False
        root=root.next
        reverseRoot=reverseRoot.next
        
    return True

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(2)
root.next.next.next.next=Node(4)

print isPalindrome(root)
''' test reverse linklist
head=reverseLinkedList(root)
while head is not None:
    print head.value
    head=head.next
'''