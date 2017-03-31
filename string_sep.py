import sys
import os

test=int(input())
n=[]
for j in range (0,test):
    n.insert(j, str(input()))

def stringseg (value):

    N= len(value)
    Even=[]
    Odd=[]

    for i in range (0, N):
        if (i % 2) == 0:
            Even.append (value[i])
        else:
            Odd.append (value[i])
    print (''.join(Even),''.join(Odd))

for k in range (0,test):
    stringseg(n[k])



