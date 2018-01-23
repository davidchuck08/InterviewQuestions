#!/usr/bin/python

class Node():
    def __init__(self,key,value, pre=None, next=None):
        self.key=key
        self.value=value
        self.pre=pre
        self.next=next
        
class DoubleLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    def isEmpty(self):
        return not self.tail
    def remove(self, node):
        if self.head==self.tail:
            self.head=None
            self.tail=None
            return
        if self.head == node:
            self.head = self.head.next
            self.head.pre=None
            return
        if self.tail.value == node.value:
            self.tail = self.tail.pre
            self.tail.next = None
            return
        node.pre.next=node.next
        node.next.pre=node.pre   
    def removeLast(self):
        self.remove(self.tail)
    def addFirst(self, node):
        if not self.head:
            self.head=node
            self.tail=node
            self.pre=None
            self.next=None
            return 
        node.pre=None
        node.next = self.head
        self.head.pre=node
        self.head = node
        return node
        
class LRUcache:
    def __init__(self, capacity):
        self.capacity=capacity
        self.size=0
        self.hash={}
        self.cache= DoubleLinkedList()
    def set(self, key, value):
        node = Node(key,value)
        if key not in self.hash:
            node = Node (key,value)
            node = self.cache.addFirst(node)
            self.hash[key] = node
            self.size+=1
            if self.size > self.capacity:
                self.size-=1
                del self.hash[self.cache.tail.key]
                self.cache.removeLast()
        else:
            self.cache.remove(self.hash[key])
            node = self.cache.addFirst(node)
            self.hash[key]=node
            
            
    def get(self, key):
        if key in self.hash and self.hash[key] is not None:
            self.cache.remove(self.hash[key])
            node=self.cache.addFirst(self.hash[key])
            self.hash[key]=node
            return self.hash[key]
        else:
            return None
        
cache = LRUcache(2)
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
print cache.get(2).value
