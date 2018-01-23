#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value = value
        self.next=None
        

def breakInto2List(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None :
        slow = slow.next
        fast=fast.next.next
       
    head1=head
    head2=slow.next
    slow.next=None
    return head1,head2

def reverseList(head):
    pre = head
    curr = head.next
    while curr is not None:
        temp = curr.next
        curr.next=pre
        pre = curr
        curr = temp
    head.next = None
    return pre
 
def reorderList(root):
    list1,list2=breakInto2List(root)
    list2 = reverseList(list2)
    res = list1
    while list2 is not None:
        temp1=list1.next
        temp2 = list2.next
        list1.next=list2
        list2.next=temp1
        list1=temp1
        list2=temp2 
    return res    
    
root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)
#root.next.next.next.next.next=Node(6)
'''
head = reverseList(root)
while head is not None:
    print head.value
    head=head.next
'''
'''
head1,head2 = breakInto2List(root)

print "Head2"
count=0
while head2 is not None:
    print head2.value,
    head2=head2.next
    count+=1
print '\nhead1'  
for x in range(count):
    print head1.value
    head1=head1.next
'''
res = reorderList(root)
while res is not None:
    print res.value
    res=res.next