#!/usr/bin/python
import heapq
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = []
    for list in lists:
        for node in list:
            if node:
                heapq.heappush(heap, (node.value, node))
    temp = Node(-1)
    head=temp
    while len(heap)>0:
        smallestNode = heapq.heappop(heap)
        print 'smallest Node: %d' %smallestNode[0]
        temp.next=smallestNode[1]
        temp=temp.next
        temp.next=None
    return head.next
node11=Node(1)
node12 =Node(2)
node13 = Node(10)
list1=[]
list1.append(node11)
list1.append(node12)
list1.append(node13)
node21=Node(3)
node22=Node(5)
list2=[]
list2.append(node21)
list2.append(node22)

lists=[]
lists.append(list1)
lists.append(list2)   
head = mergeKLists(lists)    
while head is not None:
    print head.value 
    head=head.next