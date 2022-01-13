'''
Created on 2021/06/26

@author: kentoo
'''
import math
N=int(input())
X=list(map(int,input().split()))
M=0
Y=0
C=0
sum=0
for i in range(N):
    M+=abs(X[i])
    sum+=abs(X[i])**2
    Y=math.sqrt(sum)
    C=max(abs(C),abs(X[i]))
    
print(M)
print(Y)
print(C)