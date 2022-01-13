'''
Created on 2021/08/12

@author: kentoo
'''
N=int(input())
D=list(map(int,input().split()))
sum=0
for i in range(N):
    for j in range(i,N):
        if i==j:
            continue
        sum+=D[i]*D[j]
        

print(sum)