'''
Created on 2021/11/20

@author: kentoo
'''
N,X = map(int,input().split())
A = list(map(int,input().split()))

ans = [0]*N 
ans[X-1] = 1
h = A[X-1]

for i in range(10**5):
    ans[h-1] = 1
    h = A[h-1] 
    if ans[h-1] == 2:
        break
cnt = 0
for i in range(N):
    if ans[i] == 1:
        cnt += 1
print(cnt)
    
    