'''
Created on 2021/06/18

@author: kentoo
'''
N,X=map(int,input().split())

A=list(map(int,input().split()))
B=[]
for i in range(len(A)):
    if A[i]!=X:
        B.append(A[i])
    else:
        continue

for i in range(len(B)):
    print(B[i],end=' ')

    