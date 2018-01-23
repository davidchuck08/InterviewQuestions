#!/usr/bin/python

'''
Classic Problems:
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class Node():
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

def addTwoNumber(num1,num2):
    if num1 is None or num2 is None:
        return 'invalid input'
    carry=0
    pNum1=num1
    pNum2=num2
    head=Node(0)
    ans=head
    while pNum1 is not None or pNum2 is not None or carry >0:
        curr=Node(carry)
        if pNum1 is not None:
            curr.value+=pNum1.value
        if pNum2 is not None:
            curr.value+=pNum2.value
        if curr.value >9:
            carry = 1
            curr.value%=10
        else:
            carry=0
        head.next=curr
        head=head.next
        if pNum1 is not None:
            pNum1=pNum1.next
        if pNum2 is not None:
            pNum2=pNum2.next
    return ans.next

'''
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
def addTwoNumber(node1, node2):
    carry=0
    if node1 is None or node2 is None:
        return None
    head=Node(0)
    res = head
    
    while node1 is not None or node2 is not None or carry >0:
        curr = Node(carry)
        carry=0
        if node1 is not None:
            curr.value+=node1.value
        if node2 is not None:
            curr.value+=node2.value
        if curr.value >=10:
            curr.value-=10
            carry=1
        head.next=curr
        head = curr
        if node1 is not None:
            node1=node1.next
        if node2 is not None:
            node2=node2.next
    
    return res
'''
list11=Node(2)
list12=Node(4)
list13=Node(3)
list11.next=list12
list12.next=list13

list21=Node(5)
list22=Node(6)
list23=Node(4)
list21.next=list22
list22.next=list23

res=addTwoNumber(list11, list21)
while res is not None:
    print res.value
    res=res.next
