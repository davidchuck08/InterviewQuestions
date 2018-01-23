#!/usr/bin/python

def isIsomorphic(strA, strB):
    if len(strA) == 0 or len(strB) == 0 or len(strA) != len(strB):
        return False
    map = {}
    for x in range(len(strA)):
        if strA[x] in map.keys():
            if map[strA[x]] != strB[x]:
                return False
        else:
            map[strA[x]] = strB[x]
        
    return True

strA = 'egg'
strB = 'adb'
print isIsomorphic(strA, strB)