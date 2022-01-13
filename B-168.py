'''
Created on 2021/07/17

@author: kentoo
'''
K=int(input())
S=str(input())
ans=[]
if len(S)<=K:
    print(S)
else:
    
    print(f"{S[0:K]}...")