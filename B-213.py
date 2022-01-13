'''
Created on 2021/08/11

@author: kentoo
'''
N=int(input())
A=list(map(int,input().split()))

ans={}

for i in range(N):
    ans[A[i]]=i
    
ans=sorted(ans.items())

print(int(ans[-2][1])+1)