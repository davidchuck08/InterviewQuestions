#!/usr/bin/python
from jinja2.loaders import DictLoader

def longestConsecutiveSequence(nums):
    if len(nums) == 0:
        return 0
    
    dict = {x:False for x in nums}
    maxlen = 0
    for i in dict:
        if dict[i] == False:
            curr = i 
            rightlen = 0
            while curr in dict:
                dict[i] = True
                rightlen+=1
                curr+=1
            curr = i-1 
            leftlen = 0
            while curr in dict:
                leftlen+=1
                dict[i] = True
                curr-=1
            maxlen = max(maxlen, rightlen+leftlen)
    
    return maxlen


nums = [100,4,200,1,3,2, 5]
print longestConsecutiveSequence(nums)
                