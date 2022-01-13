'''
Created on 2021/08/14

@author: kentoo
'''
N=int(input())
P=list(map(int,input().split()))

P2=sorted(P)

cnt=0
for i in range(len(P)):
    if P[i]==P2[i]:
        continue
    else:
        cnt+=1

if cnt==2 or cnt==0:
    print("YES")
else:
    print("NO")
    