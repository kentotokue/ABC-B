'''
Created on 2021/07/29

@author: kentoo
'''


H,N=map(int,input().split())

A=list(map(int,input().split()))

sum=0
for i in range(len(A)):
    sum+=A[i] 

if sum>=H:
    print("Yes")
else:
    print("No")
    
       
    