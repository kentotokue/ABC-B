'''
Created on 2021/07/04

@author: kentoo
'''
S=str(input())
T=str(input())
cnt=100000
for i in range(len(S)-len(T)+1):
    sum=0
    for j in range(len(T)):
        if S[i+j]!=T[j]:
            sum+=1
    cnt=min(cnt,sum)

print(cnt)
            
    