#!/usr/bin/python

class Stack():
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]
        self.index=-1
        
    def push(self, item):
        if len(self.list) >=self.maxSize:
            return -1
        self.list.append(item)
        self.index+=1
    def pop(self):
        if len(self.list)==0:
            return None
        item = self.list[self.index]
        self.index-=1
        return item
    
