'''
Created on 2021/10/09

@author: kentoo
'''

N,P = map(int,input().split())

A = list(map(int,input().split()))

cnt = 0
for i in range(N):
    if A[i] < P:
        cnt += 1
print(cnt)