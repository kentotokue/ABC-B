'''
Created on 2021/08/14

@author: kentoo
'''
A,B=map(int,input().split())

if B==1:
    print("0")
    exit()
sum=A
cnt=1
while sum<B:
    
    sum+=A-1
    cnt+=1

print(cnt)
    