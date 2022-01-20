'''
Created on 2022/01/20

@author: kentoo
'''
N = int(input())
sum = 1
mod = 10**9+7
for i in range(1,N+1):
    sum = (sum * i )% mod
print(sum)
    