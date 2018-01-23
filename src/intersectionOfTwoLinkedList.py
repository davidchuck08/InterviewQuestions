#!/usr/bin/python

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
def findIntersection(head1, head2):
    if head1 is None or head2 is None:
        return None
    
    len1=0
    len2=0
    p1=head1
    p2=head2
    while p1 is not None:
        len1+=1
        p1=p1.next
    while p2 is not None:
        len2+=1
        p2=p2.next
    p1=head1
    p2=head2
    diff = abs(len1-len2)
    if len1>len2:
        for i in range(diff):
            p1=p1.next
    else:
        for i in range(diff):
            p2=p2.next
    while p1 is not None and p2 is not None:
        if p1.value == p2.value:
            return p1
        else:
            p1=p1.next
            p2=p2.next
    return None

root1=Node(1)
root1.next=Node(3)
root1.next.next=Node(5)
root1.next.next.next=Node(6)

root2=Node(4)
root2.next=Node(5)

intersection = findIntersection(root1, root2)
if intersection is not None:
    print intersection.value
else:
    print None