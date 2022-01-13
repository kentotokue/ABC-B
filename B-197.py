'''
Created on 2021/06/16

@author: kentoo
'''
H,W,X,Y=map(int,input().split())
H-=1
W-=1
S=[]
for i in range(H):
    S.append(str(input()))


ud=[-1,0,1,0]
lr=[0,-1,0,1]
cnt=1
for i in range(4): #４方向
    
    nx=X
    ny=Y 
    while (True):
        ny+=ud[i]
        nx+=lr[i]
        if (nx<0 or nx>=W or ny<0 or ny>=H):
            break
        if S[ny][nx]=="#":
            break
        cnt+=1
print(cnt)   
