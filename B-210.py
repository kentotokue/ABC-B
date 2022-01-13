'''
Created on 2021/07/17

@author: kentoo
'''
N=int(input())
S=str(input())

A=0

for i in range(N):
    if S[i]=="1":
        
        A=i 
        break 


if A%2==0:
    print("Takahashi")
else:
    print("Aoki")

   
            
            
        
        



    