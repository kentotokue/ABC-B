'''
Created on 2021/06/23

@author: kentoo
'''

N,M,T=map(int,input().split())
A=[]
B=[]
for i in range(M):
    a,b=map(int,input().split())
    
    A.append(a)
    B.append(b)
    
now=0
bat=N 

for i in range(M):
    bat-=A[i]-now
    now=A[i]
    if bat<=0:
        
        break
    bat+=B[i]-A[i]
    if (bat>N):
        bat=N   
    now=B[i]
bat-=T-now
if bat<=0:
    print("No")
else:
    print("Yes")

    
    
    