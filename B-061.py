'''
Created on 2022/01/19

@author: kentoo
'''
from collections import defaultdict

N,M = map(int,input().split())
ans = defaultdict(int)
for i in range(1,N+1):
    ans[i] = 0

for i in range(M):
    a,b = map(int,input().split())
    ans[a] += 1
    ans[b] += 1


for i in ans.values():
    print(i)