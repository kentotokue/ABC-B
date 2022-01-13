'''
Created on 2021/06/15

@author: kentoo
'''

N,K=map(int,input().split())

for _ in range(K):
    if N%200==0:
        N//=200
    else:
        M=str(N)+"200"
        M=int(M)
        N=M
print(N)