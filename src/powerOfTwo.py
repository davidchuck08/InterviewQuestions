#!/usr/bin/python

def powerOfTwo(num):
    if num <=0:
        return False
    while num > 2:
        r = num >>1
        l = r <<1 
        if l!=num:
            return False
        num = num >>1
    return True

num = 2048
print powerOfTwo(num)