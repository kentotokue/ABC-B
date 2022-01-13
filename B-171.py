'''
Created on 2021/07/07

@author: kentoo
'''
N,K=map(int,input().split())

P=list(map(int,input().split()))

P.sort()
sum=0
for i in range(K):
    sum+=P[i]


print(sum)
    