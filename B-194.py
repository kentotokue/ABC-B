'''
Created on 2021/06/18

@author: kentoo
'''
N=int(input())

A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    
    A.append(a)
    B.append(b)
    
res=100000000
'''
for i in range(N):
    for j in range(N):
        res=min(res,A[i]+B[j] if i==j else max(A[i],B[j]))
'''
for i in range(N):
    for j in range(N):
        if (i==j):
            res=min(res,A[i]+B[j])
        else:
            res=min(res,max(A[i],B[j]))
print(res)