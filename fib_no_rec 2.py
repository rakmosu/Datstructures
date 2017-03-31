import sys
import os


a=0
b=1
n= int(input("No of values "))
print('you have given ', n)
if n == 0:
    print('Fibonacci series of 0 number is: 0')
elif n == 1:
    print('Fibonacci series of 1 nubers are: 0, 1')
else:
    print('\n', a, '\n', '\n', b)
    #n = n - 1
    for i in range (1,n):
        c = a + b
        a=b
        b=c
        print('\n', c)






