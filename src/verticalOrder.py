#!/usr/bin/python
import collections
class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        
def verticalOrder(root):
    
    cols = collections.defaultdict(list)
    queue=[(root,0)]
    for (node, i) in queue:
        if node is None:
            continue
        cols[i].append(node.value)
        queue.append((node.left, i-1))
        queue.append((node.right,i+1))
    for i in sorted(cols):
        print cols[i] 
        
root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.right.left = Node(5)

print verticalOrder(root) 