'''
Created on 2021/06/14

@author: kentoo
'''
N=int(input())
A=list(map(int,input().split()))

cnt=0

for i in range(N):
    if A[i]<=10:
        continue
    else:
        cnt+=A[i]-10
        

print(cnt)