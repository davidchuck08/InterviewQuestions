#!/usr/bin/python
from StdSuites.Text_Suite import word

def wordLadder(start, end, dict):
    dict.add(end)
    q = []   
    q.append((start,1))
    while q:
        curr= q.pop(0)
        currWord = curr[0] 
        currStep = curr[1]
        if currWord == end:
                return currStep
        for i in range(len(currWord)):
            part1 = currWord[:i]
            part2 = currWord[i+1:]
            for j in 'abcdefghijklmnoprrstuvwxyz':
                newWord = part1+j+part2
                if newWord in dict:
                    q.append((newWord, currStep+1))
                    dict.remove(newWord)
    
    return 0
            
def wordLadder2(start, end, dict):
    dict.add(end)
         
start='hit'
end='cog'
dict=set(['hot','dot','dog','lot','log'])

print wordLadder(start, end, dict)