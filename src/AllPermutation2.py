#!/usr/bin/python
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example, [1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

'''

import copy
def getAllpermutation2(nums):
    if nums is None or len(nums) ==0:
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
            for item in tempList:
                if item not in res:
                    res.append(item)
    return res


















'''
def getAllpermutation2(nums):
    res =[]
    if nums is None or len(nums) == 0:
        return res.keys()
    
    for num in range(len(nums)):
        if len(res)==0:
            temp = []
            temp.append(num)
            res.append(temp)
        else:
            tempList=[]
            for j in res:                
                for k in range(len(j)+1):
                    temp = copy.copy(j)
                    temp.insert(k,num)
                    tempList.append(temp) 
            for item in tempList:
                if item not in res:
                    res.append(item)
    return res
'''
nums = [1,2,1]
print getAllpermutation2(nums)