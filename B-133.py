'''
Created on 2021/08/19

@author: kentoo
'''
import math
N,D=map(int,input().split())

X=[list(map(int,input().split())) for i in range(N)]
#X.append(X[0])



cnt=0

for i in range(N):
    for j in range(i):
        sq=0
        for k in range(D):
            s=X[i][k]-X[j][k]
            sq+=s*s 
        s=math.sqrt(sq)#+0.000000000000000000005
        print(s,s**2)
        if s*s==sq:
            cnt+=1
  
'''
for i in range(N):
    dis=0
    sum=0
    for j in range(D):
        sum+=(abs((X[i][j])-(X[i+1][j])))**2
    dis=math.sqrt(sum)
        
    dis2=dis**2
    
    print(dis2,sum)
    if dis2==sum:
        cnt+=1
        
'''
print(cnt)
 