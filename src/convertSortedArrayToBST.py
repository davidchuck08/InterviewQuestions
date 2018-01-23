#!/usr/bin/python


'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
class Node():
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def buildTree(array, left, right):
    if left > right:
        return None
    mid = left+(right-left)/2
    node = Node(array[mid])
    node.left=buildTree(array, left, mid-1)
    node.right=buildTree(array, mid+1, right)
    return node
        





















'''
class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def buildTree(nums, start,end):
    if start > end:
        return None
    mid = (start+end)/2
    root = Node(nums[mid])
    root.left=buildTree(nums,start,mid-1)
    root.right=buildTree(nums,mid+1,end)
    
    return root
'''
nums=[1,2,3,4,5,6]
root = buildTree(nums, 0, len(nums)-1)
print root.value,root.left.value,root.right.value