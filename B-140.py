'''
Created on 2021/08/14

@author: kentoo
'''
N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

cnt=0
for i in range(N):
    cnt+=B[A[i]-1]

for i in range(N-1):
    if A[i]+1==A[i+1]:
        cnt+=C[A[i]-1]

print(cnt)
    