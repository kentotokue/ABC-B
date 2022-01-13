'''
Created on 2021/12/16

@author: kentoo
'''
N,M,X = map(int,input().split())
A = list(map(int,input().split()))
cnt1 = 0
for i in range(X-1,-1,-1):
    
    for j in range(M):
        if i == A[j]:
            cnt1 += 1
cnt2 = 0
for i in range(X,N):
    for j in range(M):
        if i == A[j]:
            cnt2 += 1
print(min(cnt1,cnt2))
            
            