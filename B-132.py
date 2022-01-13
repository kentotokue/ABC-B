'''
Created on 2021/08/19

@author: kentoo
'''
N=int(input())
P=list(map(int,input().split()))

cnt=0

for i in range(1,N-1):
    A=[0]*3
    A[0]=P[i-1]
    A[1]=P[i]
    A[2]=P[i+1]
    A2=sorted(A)
    if A[1]==A2[1]:
        cnt+=1

print(cnt)
    

