#!/usr/bin/python
import pdb
class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
        

def reverse(pre, next):
    last = pre.next
    curr=last.next
    while curr!=next:
        last.next = curr.next
        curr.next = pre.next
        pre.next = curr
        curr = last.next
    return pre

def reverseKNode(root, k):
    if root is None:
        return None
    fake = Node(0)
    fake.next=root
    pre = fake
    p=root
    i=0
    while p is not None:
        i+=1
        if i%k ==0:
            pre = reverse(pre,p.next)
            p = pre.next
        else:
            p=p.next
    return fake.next
def reverseKNodeStack(root, k):
    stack=[]
    p = root
    fake=Node(0)
    res=Node(0)
    index=0
    first = False
    while p is not None:
        index+=1 
        #pdb.set_trace()      
        if index %k==0:
            if first ==False:
                res.next= p
                first=True
            if fake.next is not None:
                fake.next.next=p
            
            node = p
            p=p.next
            while len(stack) > 0:
                temp = stack.pop()
                node.next=temp
                node=temp
            fake.next=node
                #pdb.set_trace()    
        else:
            stack.append(p)
            #pdb.set_trace()
            p = p.next
    
    fake.next.next=None
    return res.next

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)
root.next.next.next.next.next=Node(6)
head = reverseKNodeStack(root, 3)
while head is not None:
    #pdb.set_trace()
    print head.value
    head=head.next