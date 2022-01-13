'''
Created on 2021/07/04

@author: kentoo
'''
P=int(input())
A=[0]*10
    
for i in range(1,11):
    sum=1
    for j in range(1,i+1):
        sum*=j 
    A[i-1]=sum 

ans=0
for i in range(9,-1,-1):
    ans+=P//A[i]
    P%=A[i]

    
print(ans)  
        
    
        