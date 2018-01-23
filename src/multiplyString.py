#!/usr/bin/python
from operator import xor
def multipleString(num1, num2):
    postive = False
    num1Sign=False
    reverseNum1=''
    if num1[0]== '-':
        num1Sign= True
        reverseNum1 = num1[:0:-1]
    else:
        reverseNum1 = num1[::-1]
    num2Sign=False
    reverseNum2=''
    if num2[0]== '-':
        num2Sign= True
        reverseNum2 = num2[:0:-1]
    else:
        reverseNum2 = num2[::-1]                      
    
    negative=xor(num1Sign,num2Sign)
    
    sol = [0 for i in range(len(reverseNum1)+len(reverseNum2))]
    for i in range(len(reverseNum1)):
        for j in range(len(reverseNum2)):
            sol[i+j]+= int(reverseNum1[i])*int(reverseNum2[j])
    
    carry = 0
    for i in range(len(sol)):
        sol[i]+=carry
        if sol[i] >=10:
            carry=sol[i]/10
            sol[i]=sol[i]%10
        else:
            carry=0
    if carry >0:
        sol.append(carry)
    res=''
    if negative:
        res='-'
    copy = False
    for x in range(len(sol)-1, -1,-1):
        if copy is False and sol[x] !=0:
            copy = True
        if copy is True:
            res+=str(sol[x])
    return res
        
num1='500'
num2='-99'
print multipleString(num1, num2)
    