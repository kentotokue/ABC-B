'''
Created on 2021/07/24

@author: kentoo
'''
N,M=map(int,input().split())
A=list(map(int,input().split()))
       
sum=0

for i in A :
    sum+=i 
cnt=0
for i in A:
    if sum<=i*(4*M):
        cnt+=1

if M<=cnt:
    print("Yes")
else:
    print("No")


    