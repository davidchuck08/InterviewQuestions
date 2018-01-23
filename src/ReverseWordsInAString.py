#! /usr/bin/python

def ReverseSentence(sentence):
    wordArr = sentence.split(" ")
    length = len(wordArr)
    ans = ""
    for i in range(length):
        ans = ans + wordArr[length-1-i]
        if i < length-1:
            ans = ans + " "
    print ans

sentence = "This is a dog"    
ReverseSentence(sentence)