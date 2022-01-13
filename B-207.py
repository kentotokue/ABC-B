'''
Created on 2021/06/26

@author: kentoo
'''
A,B,C,D=map(int,input().split())

R=0
S=A 
cnt=0

for i in range(1,1000001):
    cnt+=1
    S+=B 
    R+=C 
    
    if S<=D*R:
        break
if cnt==1000000:
    print("-1")
else:
    print(cnt)

    
