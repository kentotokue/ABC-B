'''
Created on 2021/07/26

@author: kentoo
'''



A=[list(map(int,input().split())) for i in range(3)]



N=int(input())

B=[0]*N 

for i in range(N):
    B[i]=int(input())


D=[[0 for i in range(3)] for i in range(3)]

'''
for i in range(N):
    B=int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j]==B:
                D[i][j]=1
'''

for i in range(3):
    for j in range(3):
        for k in range(N):
            
            if A[i][j]==B[k]:
                print(A[i][j])
                D[i][j]=1
        
flag=False

for i in range(3):
    cnt=0
    for j in range(3):
        cnt+=D[i][j]
    if cnt==3:
        flag=True 

for i in range(3):
    cnt=0
    for j in range(3):
        cnt+=D[j][i]
    if cnt==3:
        flag=True 

cnt=0 
for i in range(3):
    cnt+=D[i][i]
    if cnt==3:
        flag=True 

cnt=0 
for i in range(3):
    cnt+=D[i][2-j]
    if cnt==3:
        flag=True 
if flag:
    print("Yes")
else:
    print("No")
        
#print(D)
        
        