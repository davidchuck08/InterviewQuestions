#!/usr/bin/python

class TreeNode():
    def __init__(self, left, right, sum=None):
        self.left = left
        self.right=right
        self.sum =sum
        self.leftChild=None
        self.rightChild=None
        

class NumArray():
    def __init__(self,nums):
        if nums is None or len(nums) == 0:
            return None
        
        self.root = self.buildTree(nums, 0, len(nums)-1)
    
    def buildTree(self, nums, left, right):
        if nums is None and len(nums) == 0:
            return None
        node = None
        if left == right:
            node = TreeNode(left,right, nums[left])
        else:
            node = TreeNode(left,right)
            mid = left + (right-left)/2
            node.leftChild = self.buildTree(nums, left, mid)
            node.rightChild = self.buildTree(nums, mid+1, right)
        
            node.sum = node.leftChild.sum + node.rightChild.sum
        return node
    
    def updateNumHelper(self, root, index,  value):
        if root is None:
            return 
        if root.left == root.right and root.left == index:
            root.sum = value
            return
        mid = root.left+(root.right-root.left)/2
        if index > mid:
            self.updateNumHelper(root.rightChild, index, value)
        else: 
            self.updateNumHelper(root.leftChild , index, value )
        
        root.sum = root.leftChild.sum+root.rightChild.sum
    def updateNume(self, index,value):
        return self.updateNumHelper(self.root, index, value)
    def sumRangeHelper(self, root, left, right):
        if root is None :
            return 0
        if right < root.left or root.right < left:
            return 0
        if left > right:
            return 0
        if left<= root.left and right >= root.right:
            return root.sum
        mid = root.left+(root.right-root.left)/2
        result = self.sumRangeHelper(root.leftChild, left, min(mid,right)) + self.sumRangeHelper(root.rightChild, max(mid+1,left),right)
        
        return result
    def sumRange(self, left, right):
        return self.sumRangeHelper(self.root, left, right)

list=[1,2,3,4,5,6,7,8,9]   
numArray = NumArray(list)
numArray.updateNume(0, 0)
print numArray.root.sum
print numArray.sumRange(1, 5)