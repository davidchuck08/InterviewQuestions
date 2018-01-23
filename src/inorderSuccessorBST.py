#!/usr/bin/python

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
 
def inorder(root,target):
    stack = []
    res = []
    done = False
   
    if root is None:
        return None
     
    if root.left is None and root.right is None:
        return None
    current = root
    index = 0
    i=0
    while done is False:
        if current.left!= None:
            print 24, current,current.left
            stack.append(current) 
            print 26, current.left
            current=current.left
            print 28, current

        else:
            if len(stack)>0:
                current=stack.pop()
                res.append(current.val)
                print res
                if len(res)>1 and res[-2] == target:
                    return res[-1]
                if current.right is not None:
                    current.append(current.right)
            else:
                done = True
    return None

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4, None, None)

print inorder(root, 2)
