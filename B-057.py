'''
Created on 2022/01/20

@author: kentoo
'''
N,M = map(int,input().split())
S = [list(map(int,input().split()))for i in range(N)]
C = [list(map(int,input().split()))for i in range(M)]

for i in range(N):
    MINC = []
    for j in range(M):
        MD = abs(S[i][0] - C[j][0]) + abs(S[i][1] - C[j][1])
        MINC.append(MD)
    print(MINC.index(min(MINC))+1)