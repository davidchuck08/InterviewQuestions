
class solution:
    def searchTarget(self,nums, target):
        if nums is None or len(nums) ==0 :
            return -1
        if target is None:
            return -1
        
        start = 0
        end = len(nums)-1
        
        while start+1 < end:
            middle = start + (end - start) /2
            if nums[middle] == target:
                return middle
            
            if (nums[start] < nums[middle]):               
                if nums[start] <= target and target <= nums[middle]:
                    end = middle
                else:
                    start = middle
            else:
                if nums[start] <=target and target <= nums[middle]:
                    start = middle
                else:
                    end = middle 
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
if __name__ == '__main__':
    nums = [5,6,7,8,0,1,2,3,4]
    target = 8
    
    sol = solution()
    print sol.searchTarget(nums, target)