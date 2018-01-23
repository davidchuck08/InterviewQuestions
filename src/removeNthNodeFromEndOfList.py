#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

def removeNthElementFromEndOfList(root, n):
    if root is None:
        return None
    
    len = 0  
    p=root
    while p is not None:
        len+=1
        p=p.next
        
    if n > len:
        n = 1 
    else:
        n = len-n
    p = root
    if n == 1:
        return root.next
    else:
        count =0
        while count < n-1:
            p=p.next
            count+=1
        p.next=p.next.next
    return root


root = Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)

head = removeNthElementFromEndOfList(root, 5) 
while head is not None:
    print head.value
    head=head.next      
            
        