'''
Created on 2022/01/14

@author: kentoo
'''

N = int(input())
K = int(input())
sum = 1
for i in range(N):
    
    if sum*2 > sum+K:
        sum += K
    else:
        sum *= 2
print(sum)