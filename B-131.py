'''
Created on 2021/08/20

@author: kentoo
'''
N,L=map(int,input().split())

T=[0]*N
for i in range(N):
    T[i]=L+(i+1)-1 


sum=0 

for i in range(N):
    sum+=T[i]
ans=1001001001

for i in range(N):
    t=sum-T[i]
    if abs(sum-t)<abs(ans):
        ans=sum-t



print(sum-ans)
        