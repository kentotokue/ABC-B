'''
Created on 2021/07/04

@author: kentoo
'''
N=int(input())

L=list(map(int,input().split()))
ans=0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i<j and j<k:
                if L[i]==L[j]:
                    continue
                if L[i]==L[k]:
                    continue
                if L[j]==L[k]:
                    continue
                if L[i]+L[j]+L[k]<=(max(L[i],L[j],L[k])*2):
                    continue
                ans+=1
                print(i,j,k)
            

print(ans)
                