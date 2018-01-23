#!/usr/bin/python

class Interval():
    def __init__(self, start, end):
        self.start=start
        self.end=end
def canAttendTheMeeting(timeList):
    timeList.sort(key=lambda x:x.start)
    for i in range(len(timeList)-1):
        if timeList[i].end > timeList[i+1].start:
            return False
    return True


interval1=Interval(0,3)
interval2=Interval(3,9)
interval3=Interval(7,10)
timeList=[]
timeList.append(interval1)
timeList.append(interval2)
timeList.append(interval3)
print canAttendTheMeeting(timeList)