'''
Created on 2021/06/21

@author: kentoo
'''

N=int(input())
A=[]
B=[]
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sum=0
for i in range(N):
    sum+=A[i]*B[i]

if sum==0:
    print("Yes")
else:
    print("No")
    