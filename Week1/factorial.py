import sys
import os


n= int(input("No of values "))
print('you have given ', n)
res=n
for i in range (1,n):
    res= (res * (n-1))
    n=n-1

print('The factorial of is: ', res)







