#!/usr/bin/python

def plusOneBinary(digits):
    if digits is None or len(digits)==0:
        return 0
    carry=1
    for i in range(len(digits)-1, -1, -1):
        digits[i]+=carry
        if digits[i] >= 10:
            carry=1
        else:
            carry=0
        digits[i]=digits[i]%10
        
    if carry == 1:
        digits.insert(0,1)
    return digits


digits=[9,9,9]
print plusOneBinary(digits)
