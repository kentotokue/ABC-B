'''
Created on 2021/06/21

@author: kentoo
'''
H,W=map(int,input().split())

A=[list(map(int,input().split())) for _ in range(H)]

a=[]
cnt=0
for i in range(H):
    a.append(min(A[i]))

M=min(a)

for i in range(H):
    for j in range(W):
        if A[i][j]>M:
            cnt+=A[i][j]-M 

print(cnt)   


