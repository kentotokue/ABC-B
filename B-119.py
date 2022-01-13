'''
Created on 2021/10/22

@author: kentoo
'''
N = int(input())
sum = 0
BC = 0
for i in range(N):
    x,u = map(str,input().split())
    
    
    if u == "JPY":
        x = int(x)
        sum += x
    else:
        x = float(x)
        BC += x

print(sum+(380000*BC))
    