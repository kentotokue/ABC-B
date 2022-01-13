'''
Created on 2021/12/18

@author: kentoo
'''
N = int(input())
D,X = map(int,input().split())
A = []
for i in range(N):
    A.append(int(input()))
cnt = 0
for i in range(N):
    DAY = 1
    j = 0
    
    while True:
        DAY = A[i]*j+1
        
        if DAY > D:
            break
        #print(DAY)
        cnt += 1
        j += 1


print(cnt+X)
    