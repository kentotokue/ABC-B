'''
Created on 2021/06/14

@author: kentoo
'''

N,K=map(int,input().split())
sum=0
for i in range(1,N+1):
    for j in range(1,K+1):
        sum+=i*100+j 

print(sum)