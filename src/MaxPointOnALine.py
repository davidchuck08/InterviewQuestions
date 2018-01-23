#!/usr/bin/python

class Point ():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
def maxPointOnALine(points):
    if points is None or len(points)==0:
        return 0
    if len(points) < 3:
        return len(points)
    map = dict()
    res=0
    length=len(points)
    for i in range(length):
        map['inf']=0
        samePoint=1
        for j in range(length):
            if i == j:
                continue
            if points[i].x == points[j].x and points[i].y != points[j].y:
                map['inf']+=1
            elif points[i].x !=points[j].x:
                slope=1.0*(points[i].y-points[j].y)/(points[i].x-points[j].x)
                if slope in map.keys():
                    map[slope]+=1
                else:
                    map[slope]=1
            else:
                samePoint+=1
        res = max(res, map[max(map, key=lambda k: map[k])]+samePoint)
        
    return res
point1=Point(1,1)
point2=Point(1,2)
point3=Point(1,4)
point4=Point(2,1)
points=[]
points.append(point1)
points.append(point2)
points.append(point3)
points.append(point4)
print maxPointOnALine(points)