'''
Created on 2021/07/31

@author: kentoo
'''
N=int(input())
S,T=map(str,input().split())


ans=""


for i in range(N):
    
    ans+=S[i]+T[i]

print(ans)