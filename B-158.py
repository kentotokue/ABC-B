'''
Created on 2021/07/26

@author: kentoo
'''
N,A,B=map(int,input().split())

S=A+B 

S1=N//S 
S2=N%S 

sum=A*S1 

if S2>=A:
    sum+=A 
else:
    sum+=S2 

print(sum)

