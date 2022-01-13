'''
Created on 2021/08/14

@author: kentoo
'''
N,K=map(int,input().split())

H=list(map(int,input().split()))

cnt=0

for i in H:
    if K<=i:
        cnt+=1
print(cnt)