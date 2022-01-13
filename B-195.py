'''
Created on 2021/06/17

@author: kentoo
'''
import math
A,B,W=map(int,input().split())
'''
upper=int(math.floor(1000*W/A))
lower=int(math.ceil(1000*W/B))

if lower>upper:
    print("UNSATISFIABLE")
else:
    print(lower,upper)
'''
a=10000000
b=0
for i in range(1,1000001):
    if A*i<=1000*W and 1000*i<=B*n:
        a=min(a,i)
        b=max(b,i)