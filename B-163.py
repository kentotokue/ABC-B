'''
Created on 2021/07/24

@author: kentoo
'''

N,M=map(int,input().split())

A=list(map(int,input().split()))

sum=0
for i in A:
    sum+=i 

if N-sum>=0:
    print(N-sum)
else:
    print("-1")