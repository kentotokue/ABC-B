'''
Created on 2022/01/13

@author: kentoo
'''
N = int(input())

L = [2,1]

for i in range(N):
    L.append(L[i]+L[i+1])
print(L[N])     