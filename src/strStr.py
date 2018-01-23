#!/usr/bin/python

def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    
    for i in range(len(haystack)):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle)-1:
                return i
    return -1

haystack = 'abbacgg'
needle = 'acg'

print strStr(haystack, needle)