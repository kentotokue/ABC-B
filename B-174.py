'''
Created on 2021/07/04

@author: kentoo
'''
import math
N,D=map(int,input().split())

P=[list(map(int,input().split())) for _ in range(N)]
cnt=0
for i in range(N):
    L=math.sqrt((P[i][0])**2+(P[i][1])**2)
    if L<=D:
        cnt+=1
        
print(cnt)
    