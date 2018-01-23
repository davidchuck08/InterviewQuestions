#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value = value
        self.next=None
        
def merge2SortedList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    fakeNode = Node(-1)
    temp = fakeNode
    while head1 is not None and head2 is not None:
        if head1.value < head2.value:
            temp.next=head1
            head1=head1.next
        else:
            temp.next=head2
            head2=head2.next
        temp = temp.next
    while head1 is not None:
        temp.next = head1
        head1=head1.next
    while head2 is not None:
        temp.next=head2
        head2=head2.next
    return fakeNode.next

list1=Node(1)
list1.next=Node(3)
list1.next.next=Node(5) 

list2=Node(2)
list2.next=Node(4)
list2.next.next=Node(6)

head = merge2SortedList(list1, list2)
while head is not None:
    print head.value
    head=head.next      