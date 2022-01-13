'''
Created on 2021/07/04

@author: kentoo
'''
N=int(input())

S=[str(input()) for _ in range(N)]

T=['AC','WA','TLE','RE']

ANS=[0]*4
for i in range(4):
    cnt=0
    for j in range(N):
        if T[i]==S[j]:
            cnt+=1
    ANS[i]=cnt

for i in range(4):
    print(f"{T[i]} x {ANS[i]}")
