'''
Created on 2021/06/21

@author: kentoo
'''
N=int(input())
point=[]
for i in range(N):
    x,y=map(int,input().split())
    point.append([x,y])
cnt=0


for i in range(N):
    for j in range(i+1,N):
        dx=point[j][0]-point[i][0]
        dy=point[j][1]-point[i][1]
        
        if (dy/dx)>=-1 and (dy/dx)<=1:
            cnt+=1

print(cnt)
     
