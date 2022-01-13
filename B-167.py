'''
Created on 2021/07/17

@author: kentoo
'''
A,B,C,K=map(int,input().split())

xa=min(A,K)
K-=xa 
xb=min(B,K)
K-=xb 
xc=K

ans=xa-xc 
print(ans)