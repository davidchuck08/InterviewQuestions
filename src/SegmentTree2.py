#!/usr/bin/python

class TreeNode():
    def __init__(self, left,right, sum=0):
        self.left=left
        self.right=right
        self.sum=sum
        self.leftChild=None
        self.rightChild=None
        
class NumArray():
    def __init__(self, nums):
        if nums is None or len(nums) == 0:
            return 
        self.root=self.buildTree(nums, 0, len(nums)-1)
        
    def buildTree(self, nums, left,right):
        if nums is None or len(nums) ==0:
            return None
        node = TreeNode(left,right)
        if left==right:
            node.sum = nums[left]
            print 'build tree',
            print node.left, node.right,node.sum
        else:
            mid = left+(right-left)/2
            node.leftChild=self.buildTree(nums, left, mid)
            node.rightChild=self.buildTree(nums,mid+1,right)
            node.sum = node.leftChild.sum + node.rightChild.sum
            print 'build tree',
            print node.left,node.right,node.sum
        
        return node
    
    def updateNumHelper(self, root, index, value):
        if root is None:
            print 'root is None'
            return
        
        mid = root.left + (root.right-root.left)/2
        print root.left, root.right
        print 'index',
        print index
        print 'mid', 
        print mid
        if mid >= index:
            print 'left child'
            self.updateNumHelper(root.leftChild, index, value)
        else:
            print 'right child'
            self.updateNumHelper(root.rightChild, index, value)
        if root.left == root.right and  root.left == index:
            print 'change value',
            print root.left,root.right
            root.sum = value
            return
        if root.leftChild is not None and root.rightChild is not None:
            print root.left,root.right
            print root.leftChild.sum,  root.rightChild.sum
            root.sum = root.leftChild.sum + root.rightChild.sum
        return
    
    def updateNum(self,index, value):
        self.updateNumHelper(self.root, index, value)
        
    def sumRange(self, left,right):
        return self.sumRangeHelper(self.root, left, right) 
     
    def sumRangeHelper(self, root, left,right):
        if root is None:
            return 0
        if left> right:
            return 0
        if root.right < left or root.left > right:
            return 0
        if root.left >= left and root.right <= right:
            return root.sum
        mid = root.left + (root.right-root.left)/2
        result = self.sumRangeHelper(root.leftChild, left, min(mid,right))+self.sumRangeHelper(root.rightChild, max(mid+1, left), right)
        return result
list = [1,2,3,4,5,6,7,8,9]
#list=[1,2,3]
numArray = NumArray(list)
#numArray.updateNum(0, 5)
print numArray.root.sum
print numArray.sumRange(0, 1)