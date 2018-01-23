#! /usr/bin/python

a=[1,2,3,4,5,6,7]
k=4
for i in range(k):
    for j in range(len(a)-1):
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
print a