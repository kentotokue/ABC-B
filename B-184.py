'''
Created on 2021/06/23

@author: kentoo
'''
N,X=map(int,input().split())

S=str(input())

for i in range(N):
    if S[i]=="o":
        X+=1
    elif S[i]=="x":
        X-=1
        if X<=0:
            X=0
        

print(X)