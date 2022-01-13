'''
Created on 2021/06/18

@author: kentoo
'''
N=int(input())
INF=1<<30
ans=INF
Q=[]
for i in range(N):
    A,P,X=map(int,input().split())
    if X>A and ans>P:
        ans=P
if ans==INF:
    ans= -1
print(ans)
    




    