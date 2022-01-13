'''
Created on 2021/07/17

@author: kentoo
'''
N=int(input())
A=list(map(int,input().split()))

sum=1
for i in A:
    if i==0:
        print("0")
        exit()
for i in range(N):
    
    sum*=A[i]
    if sum>10**18:
        print("-1")
        exit()
        
    


print(sum)
    