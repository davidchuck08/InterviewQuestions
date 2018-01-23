#!/usr/bin/python
from Tkconstants import LEFT
from test.test_iterlen import NoneLengthHint
from StdSuites.AppleScript_Suite import result

class Node():
    def __init__(self,value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        
def postOrder(root):
    if root is None:
        return 
    result = []
    if root.left is not None:
        result = result+postOrder(root.left)
    if root.right is not None:
        result= result+postOrder(root.right)

    result.append(root.value)        
    return result


root =Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.right.right = Node(5)

print postOrder(root)