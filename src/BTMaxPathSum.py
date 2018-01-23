#!/usr/bin/python

'''
Given a binary tree, find the maximum path sum. 
The path may start and end at any node in the tree. 
For example, given the below binary tree

       1
      / \
     2   3
the result is 6.
'''
import sys
from test._mock_backport import right
class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        
class Path():
    def __init__(self,root):
        self.root=root
        self.maxSum=-sys.maxint+1
    def calculate(self, node):
        if node is None:
            return 0
        leftSum=self.calculate(node.left)
        rightSum=self.calculate(node.right)
        self.maxSum=max(self.maxSum,max(rightSum,leftSum)+node.value)
        return max(rightSum,leftSum)+node.value
'''
import sys
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
    
        
def calculateSum(root, maxSum):
    if root is None:
        return 0
    
    leftSum=calculateSum(root.left, maxSum)
    rightSum =calculateSum(root.right, maxSum)
    
    current = max(root.value, max(leftSum,rightSum)+root.value)
    
    maxSum = max(current, leftSum+rightSum+root.value)
    calculateSum.res = max(calculateSum.res,maxSum)
    return current

def getMaxSum(root):
    maxSum=-sys.maxint+1
    calculateSum.res=-sys.maxint+1
    calculateSum(root, maxSum)
    print  calculateSum.res
'''
root=Node(1)
root.left=Node(2)
root.right=Node(3)

path = Path(root)
print path.calculate(root)