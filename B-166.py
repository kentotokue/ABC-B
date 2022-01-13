'''
Created on 2021/07/24

@author: kentoo
'''
N,K=map(int,input().split())


A=[0]*(N+1) 

for i in range(K):
    d=int(input())
    S=list(map(int,input().split()))
    
    for j in S:
        
        A[j]=1 
cnt=0
for i in range(1,len(A)):
    if A[i]==0:
        cnt+=1

print(cnt)
        
    