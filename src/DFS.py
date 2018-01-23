
'''
DFS
'''
class solution:
    def __init__(self):
        self.result=[]
    def DFS(self, nums, start, valueList):
        if nums is None or len(nums)==0:
            return None
        self.result.append(valueList)
        for i in range(start, len(nums)):
            self.DFS(nums,i+1,valueList+[nums[i]])
'''
import copy
class solution:
    def __init__(self):
        self.result = []
    def DFS(self, nums):
        list = []
        if nums is None or len(nums) == 0:
            return self.result
        nums=sorted(nums)
        self.subsetHelper( list, nums, 0)
        print self.result
        
    def subsetHelper(self, list, nums, pos):
        
        self.result.append(copy.copy(list))
        
        for i in range(pos,len(nums)):
            list.append(nums[i])
            self.subsetHelper( list,nums,i+1)
            list.pop(len(list)-1)
 '''           
if __name__=='__main__':
    sol = solution()
    nums = [1,2,3,4]
    #sol.DFS(nums)
    sol.DFS(nums,0,[])
    print sol.result