#!/usr/bin/python
'''
This post shows how to implement a stack by using an array.

The requirements of the stack are: 
1) the stack has a constructor which accept a number to initialize its size, 
2) the stack can hold any type of elements, 
3) the stack has a push() and a pop() method.

'''

class Stack():
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.stack=[0 for i in range(maxSize)]
        self.size=0
    
    def push(self, item):
        if self.size >= self.maxSize:
            return 'stack is full'
        self.stack[self.size]= item
        self.size+=1
    
    def pop(self):
        if self.size == 0:
            return 'stack is empty'
        self.size-=1
        return self.stack[self.size]
    
        
    
stack=Stack(10)
stack.push(1)
print stack.size
stack.push(2)
stack.push(3)
print stack.size
print stack.stack
print stack.pop()
print stack.size
print stack.stack



















'''
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
    
'''