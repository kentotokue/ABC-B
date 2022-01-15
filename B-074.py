'''
Created on 2022/01/15

@author: kentoo
'''
N = int(input())
K = int(input())
X = list(map(int,input().split()))

sum = 0
for i in range(N):
    d = abs(X[i]-K)
    if X[i] > d:
        sum += d*2
    else:
        sum += X[i]*2 
print(sum)