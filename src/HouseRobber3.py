#!/usr/bin/python

class Node():
    def __init__(self, val, right=None, left=None):
        self.val=val
        self.right=right
        self.left=left

def dfs(root):
    if root is None:
        return 0
    #picking up root
    val=0
    if root.left is not None:
        val+=dfs(root.left.left)+dfs(root.left.right)
    if root.right is not None:
        val+= dfs(root.right.left)+dfs(root.right.right)
    result1 = root.val+val
    
    #does not pick root
    result2 = dfs(root.left) + dfs(root.right)
    
    return max(result1, result2)

root = Node(4)
root.left = Node(10)
root.left.left = Node(2)
root.left.left.left = Node(3)

print dfs(root)