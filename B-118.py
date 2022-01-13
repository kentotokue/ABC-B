'''
Created on 2021/11/25

@author: kentoo
'''
N,M = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]
ans = {}

for i in range(N):
    for j in range(1,A[i][0]+1):
        
        if A[i][j] in ans:
            ans[A[i][j]] += 1
        else:
            ans[A[i][j]] = 1
#print(ans)
cnt = 0
for i in ans.values():
    if i == N :
        cnt += 1
print(cnt)