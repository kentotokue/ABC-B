'''
Created on 2021/11/27

@author: kentoo
'''
N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
MX = max(x)
y = list(map(int,input().split()))
MY = min(y)

flag = False
for i in range(X+1,Y+1):
    if MX < i and MY >= i:
        print("No War")
        exit()


print("War")
       

    
        