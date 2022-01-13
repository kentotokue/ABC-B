'''
Created on 2021/11/26

@author: kentoo
'''
N,T = map(int,input().split())
L = [list(map(int,input().split()))for i in range(N)]

ans = 100100100
for i in range(N):
    if L[i][1] <= T:
        ans = min(ans,L[i][0])
if ans == 100100100:
    print("TLE")
else:
    print(ans)