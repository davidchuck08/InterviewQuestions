#!/usr/bin/python


'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

For example,
 Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''
def fractionalDecimal(numerator, denominator):
    if numerator is None or denominator is None:
        return 'Input Error'
    if denominator == 0:
        return 'Input Error: denominator is 0'
    if numerator == 0:
        return 0
    
    negative=False
    if numerator*denominator<0:
        negative=True
    numList=[]
    reminder=dict()
    currLoc=0
    loopStr=''
    
    while True:
        numList.append(str(numerator/denominator))
        numerator=10*(numerator%denominator)
        currLoc+=1
        if numerator in reminder.keys():
            preLoc=reminder[numerator]
            loopStr=''.join(numList[preLoc:currLoc])
            break
        else:
            reminder[numerator]=currLoc
    ans=''
    if negative==True:
        ans='-'
    ans+=numList[0]
    if len(numList)>1:
        ans+='.'
    if len(loopStr)>0:
        ans+=''.join(numList[1:len(numList)-len(loopStr)])+'('+loopStr+')'
    else:
        ans+=''.join(numList[1:])
        
    return ans









'''
def fractionalDecimal(numerator, denominator):
    if denominator == 0:
        return ''
    if numerator == 0:
        return '0'
    negative=False
    if numerator*denominator < 0:
        negative=True
        numerator=abs(numerator)
        denominator=abs(denominator)
    numList=[]
    reminder=dict()
    currLoc=0
    loopStr=''
    
    while True:
        numList.append(str(numerator/denominator))
        numerator=10*(numerator%denominator)
        currLoc+=1
        if numerator == 0:
            break
        if numerator in reminder.keys():
            preLoc=reminder[numerator]
            loopStr=''.join(numList[preLoc:currLoc])
            break
        else:
            reminder[numerator]=currLoc
    ans=''
    if negative:
        ans='-'
    ans+=numList[0]
    if len(numList)>1:
        ans+='.'
    if len(loopStr)>0:
        ans+=''.join(numList[1:len(numList)-len(loopStr)])+'('+loopStr+')'
    else:
        ans+=''.join(numList[1:])
    return ans
'''            
numerator=10
denominator=3
print fractionalDecimal(numerator, denominator)