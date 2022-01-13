'''
Created on 2021/08/21

@author: kentoo
'''
N=int(input())

A=[]

for i in range(N):
    S,P=map(str,input().split())
    P=-int(P)
    A.append([S,P,i])
A.sort()
print(A)
for i in range(N):
    print(A[i][2]+1)
