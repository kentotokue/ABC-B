'''
Created on 2021/10/30

@author: kentoo
'''
N = int(input())
T = [list(map(int,input().split())) for i in range(N-1)]

ans = {}
for i in range(N-1):
    if T[i][0] in ans:
        ans[T[i][0]] += 1
    else:
        ans[T[i][0]] = 1
    if T[i][1] in ans:
        ans[T[i][1]] += 1
    else:
        ans[T[i][1]] = 1
    
m = max(ans.values())
if N-1 == m:
    print("Yes")
else:
    print("No")

