#!/usr/bin/python
'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned 
in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; 
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)    -3    3
-5    -10    1
10    30    -5 (P)
'''
from matplotlib.sankey import DOWN

def dungeonGame(nums):
    col=len(nums[0])
    row=len(nums)
    hp= [[0 for j in range(col)] for i in range(row)]
    hp[row-1][col-1]=max(1-nums[-1][-1], 1)
    
    for i in range(row-1, -1,-1):
        for j in range(col-1,-1,-1):
            down=None
            if i+1 < row:
                down=max(1, hp[i+1][j]-nums[i][j])
            right=None
            if j+1 < col:
                right=max(1,hp[i][j+1]-nums[i][j])
            if down and right:
                hp[i][j]=min(down,right)
            elif down:
                hp[i][j]=down
            elif right:
                hp[i][j]=right
    return hp[0][0]
    
    

'''
def dungeonGame(nums):
    col = len(nums)
    row = len(nums[0])

    hp =[[0 for i in range(row)] for j in range(col)]
    hp[row-1][col-1] = max(1-nums[row-1][col-1],1)
    
    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            down = None
            if i+1 < row:
                down = max(1, hp[i+1][j]-nums[i][j])
            right = None
            if j+1 < col:
                right = max(1, hp[i][j+1]-nums[i][j])
            if down and right:
                hp[i][j]=min(down, right)
            elif down:
                hp[i][j] = down
            elif right:
                hp[i][j] = right
    print hp
    return hp[0][0]
'''
c1=[-2,-5,10]
c2=[-3,-1,30]
c3=[3,1,-5]
nums = []
nums.append(c1)
nums.append(c2)
nums.append(c3)
print nums
print dungeonGame(nums)