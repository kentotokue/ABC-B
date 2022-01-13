'''
Created on 2021/07/30

@author: kentoo
'''
N,K,M=map(int,input().split())
A=list(map(int,input().split()))


sum=0
for i in range(N-1):
    sum+=A[i]

ans=(N*M)-sum 



if ans<=K:
    
    print(max(ans,0))
else:
    print("-1")
