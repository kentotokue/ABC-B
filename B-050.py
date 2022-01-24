'''
Created on 2022/01/23

@author: kentoo
'''
N = int(input())
T = list(map(int,input().split()))
M = int(input())
D = [list(map(int,input().split()))for i in range(M)]

TS = sum(T)

for i in range(M):
    if T[D[i][0]-1] >= D[i][1]:
        print(TS + (D[i][1]-T[D[i][0]-1]))
    else:
        print(TS - (T[D[i][0]-1]-D[i][1]))
