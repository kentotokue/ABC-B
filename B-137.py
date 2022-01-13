'''
Created on 2021/08/14

@author: kentoo
'''
K,X=map(int,input().split())

S=X-K+1
E=X+K-1 

for i in range(S,E+1):
    print(i,end=" ")
    