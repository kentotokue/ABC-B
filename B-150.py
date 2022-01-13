'''
Created on 2021/07/30

@author: kentoo
'''
N=int(input())
S=str(input())

cnt=0

for i in range(0,N-2):
    if S[i:i+3]=="ABC":
        cnt+=1
    else:
        continue

print(cnt)