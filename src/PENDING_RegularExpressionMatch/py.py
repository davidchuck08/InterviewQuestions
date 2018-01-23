#!/usr/bin/python

def isMatch(s, p):
    if len(p) == 0:
        return len(s) == 0
    if 