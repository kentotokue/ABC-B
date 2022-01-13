'''
Created on 2021/06/19

@author: kentoo
'''

N,X=map(int,input().split())
D=[]
sum=0
cnt=0
flag=False
for i in range(N):
    V,P=map(int,input().split())
    
    
    
    sum+=V*P
    cnt+=1
    if sum>X*100:
        flag=True
        break

if flag:
    print(cnt)
else:
    print("-1")
    




    