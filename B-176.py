'''
Created on 2021/07/04

@author: kentoo
'''
N=int(input())

NS=str(N)
sum=0
for i in range(len(NS)):
    sum+=int(NS[i])

if sum%9==0:
    print("Yes")
else:
    print("No")