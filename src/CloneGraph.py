#!/usr/bin/python

'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
'''

class Node():
    def __init__(self,label):
        self.label=label
        self.neighbors=[]
        
def cloneGraph(head):
    if head is None:
        return None
    newHead=Node(head.label)
    map=dict()
    map[head]=newHead
    queue=[]
    queue.append(head)
    
    while len(queue)>0:
        curr=queue.pop(0)
        for neighbor in curr.neighbors:
            if neighbor not in map:
                copy=Node(neighbor.label)
                map[curr].neighbors.append(neighbor)
                queue.append(neighbor)
                map[neighbor]=copy
            else:
                map[curr].neighbors.append(map[neighbor])
    return newHead























'''
class Node():
    def __init__(self,label):
        self.label=label
        self.neighbors=[]
        
def cloneGraph(head):
    if head is None:
        return None
    map = {}
    queue=[]
    queue.append(head)
    newHead = Node(head.label)
    map[head]=newHead
    while len(queue) >0:
        curr = queue.pop(0)
        for neighbor in curr.neighbors:
            if neighbor not in map:
                copy = Node(neighbor.label)
                map[curr].neighbors.append(copy)
                map[neighbor]=copy
                queue.append(neighbor)
            else:
                map[curr].neighbors.append(map[neighbor])
    return newHead
'''
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node4)
node4.neighbors.append(node1)
node4.neighbors.append(node3)
node4.neighbors.append(node2)
node3.neighbors.append(node1)
node3.neighbors.append(node4)

newNode1=cloneGraph(node1)   
print 'label: ' +str(newNode1.label)
newNode2=None
for node in newNode1.neighbors:
    if node.label == 2:
        newNode2=node
    print node.label   
    
print 'label: '+ str(newNode2.label) 
for node in newNode2.neighbors:
    print node.label