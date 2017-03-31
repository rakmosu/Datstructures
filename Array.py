import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

a=n
out=[ ]

for i in range (0,n):
    out.append(arr[n - 1])
    n=n-1

var = str(out[0])
for j in range (1, a):
    var= var+' '+ str(out[j])

print (var)
