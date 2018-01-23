

class Solution():
    def findMin(self,nums):
        start = 0 
        end = len(nums)-1
        while start+1 < end:
            mid = start+(end-start)/2
            if nums[mid] > start:
                start = mid
            else:
                end = mid
                
        if nums[start]>nums[end]:
            return nums[end]
        else:
            return nums[start]
        
if __name__ == '__main__':
    nums = [4,4,5,8,10,0,0,1,2,3]
    sol = Solution()
    print sol.findMin(nums)