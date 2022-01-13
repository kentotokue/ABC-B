'''
Created on 2021/06/19

@author: kentoo
'''
N,S,D=map(int,input().split())
J=[]
flag=False
for i in range(N):
    X,Y=map(int,input().split())
    J.append([X,Y])
    
for i in range(N):
    if int(J[i][0])<S and int(J[i][1])>D:
        flag=True

if flag:
    print("Yes")
else:
    print("No")
    