#!/usr/bin/python

class Interval():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    
def minMeetingRoom(intervals):
    if intervals is None or len(intervals) == 0:
        return 0
    start=[]
    end=[]
    for interval in intervals:
        start.append(interval.start)
        end.append(interval.end)
        
    start.sort()
    end.sort()
    s = 0
    e = 0
    available=0
    numRoom = 0
    print start
    print end 
    while s < len(start):
        if start[s] < end[e]:
            if available == 0:
                numRoom+=1
            else:
                available-=1
                print 'minus available: ' + str(available)
            s+=1
                
        else:
            available+=1
            print start[s]
            print end[e]
            print 'available: ' + str(available)
            e+=1
            
    return numRoom

interval1=Interval(0,5)
interval2=Interval(5,10)
interval3=Interval(15,20)
intervals = []
intervals.append(interval1)
intervals.append(interval2)
intervals.append(interval3)

print minMeetingRoom(intervals)           
        