#!/usr/bin/python
'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''
import copy

def getAllPermutation(nums):
    if nums is None or len(nums) == 0:
        return None
    res=[]
    
    for i in range(len(nums)):
        if len(res) == 0:
            res.append([nums[i]])
        else:
            tempList=[]
            for j in res:
                for k in range(len(j)+1):
                    temp=copy.copy(j)
                    temp.insert(k, nums[i])
                    tempList.append(temp)
            res+=tempList
    return res
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
def getAllPermutation(nums):
    if nums is None or len(nums)==0:
        return None
    
    res=[]
    for i in range(len(nums)):
        if len(res) ==0:
            temp = []
            temp.append(nums[i])
            res.append(temp)
            
            
        else:
            tempList=[]
            for j in res:                
                for k in range(len(j)+1):
                    temp = copy.copy(j)
                    temp.insert(k,nums[i])
                    tempList.append(temp)   
       
            res+=tempList
    return res
'''
nums=[1,2,3]
print getAllPermutation(nums)

            