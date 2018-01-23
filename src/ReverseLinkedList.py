from django.template.defaultfilters import last
class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        newNode = Node(value, None)
        newNode.next = self.head
        self.head = newNode
        
    def printList(self):
        temp =self.head
        while temp != None:
            print temp.value
            temp = temp.next
            
    def reverseList(self):
        last = None      
        temp = self.head
        while temp is not None:
            next = temp.next
            temp.next = last
            last = temp
            temp = next
            
        self.head = last
        
if __name__ == '__main__':
    linkList = LinkedList()
    linkList.push(10)
    linkList.push(20)
    linkList.push(30)
    linkList.push(40)
    linkList.push(50)
    
    linkList.printList()
    
    linkList.reverseList()
    linkList.printList()
                