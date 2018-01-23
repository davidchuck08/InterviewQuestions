#define single linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def __init__(self):
        pass
    def addTwoNumber(self, list1, list2):
        carry = 0
        head = ListNode(0)
        sol = head
        
        while list1 or list2 or carry:
            sum = carry
            carry = 0
            if list1:
                print 'list1'
                print list1.val
                sum +=list1.val
                list1 = list1.next
            if list2:
                print 'list2'
                print list2.val
                sum+=list2.val
                list2=list2.next
            if sum >=10:
                sum = sum-10
                carry =1
            print 'sum %d' %(sum)
            
            sol.next = ListNode(sum)
            sol = sol.next

        return head.next
    
if __name__ == '__main__':
    number11 =ListNode(1)
    number12 = ListNode(1)
    number13 = ListNode(1)
    number11.next = number12
    number12.next = number13
    
    number21=ListNode(9)
    number22 = ListNode(0)
    number21.next = number22
    number23 = ListNode(1)
    number22.next = number23
    
    sol = Solution()
    firstNode =sol.addTwoNumber(number11, number21)
    while firstNode is not None:
        print firstNode.val
        firstNode = firstNode.next
    