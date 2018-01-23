#!/usr/bin/python
class Node ():
    def __init__(self,value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right


def kthSmallestElement(root, k):
    if k==0 or root is None:
        return
    stack=[]
    node = root
    while len(stack)>0 or node != None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k-=1
                if k==0:
                    return node.value
                node = node.right
    return None
root = Node(4)
root.left=Node(2)
root.left.left=Node(1)
root.left.right=Node(3)
root.right=Node(5)

print kthSmallestElement(root, 3)
