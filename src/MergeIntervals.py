#!/usr/bin/python
from locale import _grouping_intervals
class Interval():
    def __init__(self, start, end):
        self.start=start
        self.end=end
        
def mergeInterval(intervals):
    res = []
    if len(intervals) == 0:
        return res
    length = len(intervals)
    for interval in intervals:
        if len(res) == 0:
            res.append(interval)
            
        else:
            current = res.pop()
            if current.start <= interval.start and interval.start <= current.end:
                current.end = max(interval.end, current.end)
                res.append(current)
            else:
                res.append(current)
                res.append(interval)
    return res

def insertInterval(intervals, newInterval):
    index = len(intervals)-1
    merged = False
    while index > 0:
        if merged == True:
            newInterval = intervals.pop()
        current = intervals.pop()
        if current.start <=newInterval.start and newInterval.start <= current.end:
            current.end = max(current.end, newInterval.end )
            merged = True
            intervals.append(current)
            index = len(intervals)-1
        elif newInterval.start<=current.start and current.start <=newInterval.end:
            current.start = min(current.start, newInterval.start)
            current.end = max(current.end, newInterval.end)
            merged = True
            intervals.append(current)
            index = len(intervals)-1
        else:
            merged = False
            intervals.append(current)
            intervals.append(newInterval)
            break
        
    return intervals    

 
input = [[1,3],[2,6],[8,10],[4,6], [15,18]]
intervalInput = []

input = sorted(input,key=lambda x:x[0])
for item in input:
    interval = Interval(item[0],item[1])
    intervalInput.append(interval)

res = mergeInterval(intervalInput)
for x in res:
    print '[%d, %d],' %(x.start, x.end)

print 'insert interval'
newInterval= Interval(11,13)
print 'new Interval [%d %d]' %(newInterval.start, newInterval.end)

res = insertInterval(res, newInterval)
res = sorted(res, key=lambda x:x.start)
for x in res:
    print '[%d, %d]' %(x.start, x.end),
        