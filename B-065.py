'''
Created on 2022/01/18

@author: kentoo
'''
N = int(input())
A = [int(input()) for i in range(N)]

btn = 1
cnt = 0
for i in range(N):
    btn = A[btn-1]
    cnt += 1
    if btn == 2:
        print(cnt)
        exit()
print(-1)