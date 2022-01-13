'''
Created on 2021/12/11

@author: kentoo
'''
A = list(map(int,input().split()))
A.sort()
M = A[-1]
K = int(input())
ans = M
for i in range(K):
    ans *=  2

print(ans + A[0] + A[1])